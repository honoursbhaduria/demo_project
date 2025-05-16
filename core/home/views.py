from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *  # Ensure the `Student` model exists in `models.py`
from .serializers import *  # Ensure the `StudentSerializer` exists in `serializers.py`


@api_view(['GET'])
def home(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response({
        'status': 200,
        'payload': serializer.data
    })


@api_view(['POST'])
def post_student(request):
    serializer = StudentSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response({
            'status': 200,
            'payload': serializer.data,
            'message': "Student created successfully"
        })
    else:
        return Response({
            'status': 400,
            'message': "Something went wrong",
            'errors': serializer.errors
        })


@api_view(['PUT'])
def update_student(request, id):
    try:
        student_obj = Student.objects.get(id=id)  # Ensure `id` is passed correctly in the URL

        serializer = StudentSerializer(student_obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 200,
                'payload': serializer.data,
                'message': "Student updated successfully"
            })
        else:
            return Response({
                'status': 400,
                'message': "Something went wrong",
                'errors': serializer.errors
            })
    except Student.DoesNotExist:  # This exception is handled correctly
        return Response({
            'status': 404,
            'message': "Student not found / invalid ID"
        })

