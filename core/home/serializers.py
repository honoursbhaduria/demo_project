from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


    def validate(self, data):
        if data['age'] < 0:
            raise serializers.ValidationError("Age cannot be negative")
        if data['name'] == "":
            raise serializers.ValidationError("Name cannot be empty")
        if data['email'] == "":
            raise serializers.ValidationError("Email cannot be empty")












































        # Documentation reference:

        # Specify fields to include or exclude in the serializer:
        # fields = ['name', 'age', 'email', 'phone', 'address']
        # exclude = ['created_at', 'updated_at']

        # Use extra_kwargs to enforce additional (mandatory fields):
        # extra_kwargs = {
        #     'name': {'required': True},
        #     'age': {'required': True},
        #     'email': {'required': True},
        # }

        # The extra_kwargs ensure that the 'name', 'age', and 'email' fields
        # are mandatory when using the serializer (e.g., in API POST requests),
        # even if they are not marked as blank=False or null=False in the model.