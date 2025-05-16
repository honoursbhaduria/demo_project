from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'



    # remember section of the docs :--  

        # fields = ['name', 'age', 'email', 'phone', 'address']
        # exclude = ['created_at', 'updated_at']
        # extra_kwargs = {
        #     'name': {'required': True},
        #     'age': {'required': True},
        #     'email': {'required': True},      }
        #   USE OF THE  -------extra_kwargs ---------the name, age, and email fields from the student model
        #   to be required when using the serializer (e.g., in API POST requests). 
        #   Even if they are not marked as blank=False or null=False in the model, 
        #   the serializer will treat them as mandatory.