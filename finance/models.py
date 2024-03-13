from django.db import models
from student.models import Student

class Finance(models.Model):
     student = models.ForeignKey(Student ,  on_delete=models.CASCADE, null=True)
     balance = models.FloatField()


# Create your models here.
