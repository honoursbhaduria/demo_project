# Generated by Django 5.2 on 2025-05-16 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_student_studentsinfo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Studentsinfo',
            new_name='Student',
        ),
    ]
