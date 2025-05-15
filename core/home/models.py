from django.db import models


class Studentsinfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default = 18)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name