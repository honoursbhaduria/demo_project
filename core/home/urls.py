from django.contrib import admin
from django.urls import path, include
from .views import home, post_student, update_student

urlpatterns = [
   path('', home, name='home'),
   path('student/', post_student, name='student'),
   path('update-student/<int:id>/', update_student, name='update_student'),
]


