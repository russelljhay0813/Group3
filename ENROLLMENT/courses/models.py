from django.db import models

class Course(models.Model):
    code = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    desciption = models.TextField(blank=True)

    def __str__(self):
        return self.name
