from django.db import models
from student.models import Student


class Activity(models.Model):
   activityname=models.CharField( max_length=150, unique =   True)
   student = models.ForeignKey(Student ,  on_delete=models.CASCADE)
   def __str__(self) -> str:
          return self.activityname
            
   

        
                       


class Disciplinary(models.Model):
   student = models.ForeignKey(Student ,  on_delete=models.CASCADE)
   case = models.CharField( max_length=150, unique = True)
   resolved= models.BooleanField(default=False)
   
   def __str__(self) -> str:
       return self.case



class Damages(models.Model):
    student = models.ForeignKey(Student ,  on_delete=models.CASCADE)
    damagecaused=models.CharField( max_length=150, unique = True)
    repaired = models.BooleanField(default=False)

    def __str__(self):
      return self.damagecaused


class Hostel(models.Model):
    student = models.ForeignKey(Student ,  on_delete=models.CASCADE)
    checkindate = models.DateField(auto_now = True)
    checkoutdate = models.DateField(auto_now = True)
    hostelname=models.CharField( max_length=150)

    def __str__(self):
      return self.hostelname
    


class Games(models.Model):
    student = models.ForeignKey(Student ,  on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity ,  on_delete=models.CASCADE)


    def __str__(self):
     return self.activity.activityname










# Create your models here.
