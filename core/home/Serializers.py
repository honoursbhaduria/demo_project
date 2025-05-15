from rest_framework import serializers
from .models import *

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'
        # fields = ['name', 'age', 'email', 'phone', 'address']
        # exclude = ['created_at', 'updated_at']
        # extra_kwargs = {
        #     'name': {'required': True},
        #     'age': {'required': True},
        #     'email': {'required': True},      }


