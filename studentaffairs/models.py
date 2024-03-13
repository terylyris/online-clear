from django.db import models
from student.models import Student


class Activity(models.Model):
   activityname=models.CharField( max_length=150, unique =   True)
   Student = models.ForeignKey(Student ,  on_delete=models.CASCADE)


class Disciplinary(models.Model):
   Student = models.ForeignKey(Student ,  on_delete=models.CASCADE)
   case = models.CharField( max_length=150, unique = True)
   resolved= models.BooleanField(default=False)


class Damages(models.Model):
    Student = models.ForeignKey(Student ,  on_delete=models.CASCADE)
    damagecaused=models.CharField( max_length=150, unique = True)
    repaired = models.BooleanField(default=False)


class Hostel(models.Model):
    Student = models.ForeignKey(Student ,  on_delete=models.CASCADE)
    checkindate = models.DateField(auto_now = True)
    checkoutdate = models.DateField(auto_now = True)
    hostelname=models.CharField( max_length=150)


class Games(models.Model):
    Student = models.ForeignKey(Student ,  on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity ,  on_delete=models.CASCADE)









# Create your models here.
