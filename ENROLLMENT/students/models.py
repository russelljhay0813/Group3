from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    year_level = models.IntegerField()

    def __str__(self):
        return f"{self.first_name}{self.last_name}"