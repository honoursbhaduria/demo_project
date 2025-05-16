from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer


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
            'payload': serializer.data
            'message': "Student created successfully" 
        })
    else:
        return Response({
            'status': 400,
            'message': "Something went wrong",
            'errors': serializer.errors
        })
