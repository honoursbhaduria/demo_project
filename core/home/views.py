from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view
def home(request):
    return Response({
        'status' : 200 , 'meassage' : 'Welcome to the API' , 'data' : {
            'name' : 'Django Rest Framework API',
            'version' : '1.0.0',
            'author' : 'Your Name'
        }
    })

    