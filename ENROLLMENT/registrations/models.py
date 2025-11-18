from django.db import models
from students.models import Student
from courses.models import Course

class Registration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.CharField(max_length=20)
    school_year = models.CharField(max_length=10)
    date_registered = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.course}"