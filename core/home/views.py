 
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def home(request):
    return Response({
        'status': 200,
        'message': 'Welcome to the API'  
    })
