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


