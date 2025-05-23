from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *  
from .serializers import * 

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
        student_obj = Student.objects.get(id=id)  

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


@api_view(['DELETE'])
def delete_student(request, id):
    try:
        student_obj = Student.objects.get(id=id)
        student_obj.delete()
        return Response({
            'status': 200,
            'message': 'Student deleted successfully'
        })
    except Student.DoesNotExist:
        return Response({
            'status': 404,
            'message': 'Invalid id / Student not found'
        })


