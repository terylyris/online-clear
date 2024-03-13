from django.db import models


class School(models.Model):
    name = models.CharField( max_length=150, unique =   True)


class Department(models.Model):
     name = models.CharField( max_length=150, unique = True)
     school = models.ForeignKey(School ,  on_delete=models.CASCADE)


class Course(models.Model):
     name = models.CharField( max_length=150, unique = True)
     department =models.ForeignKey(Department ,  on_delete=models.CASCADE)
     unitsdone = models.IntegerField()


class Student(models.Model):
    regNo = models.CharField( max_length=150, unique = True)
    name = models.CharField( max_length=150 )
    course = models.ForeignKey(Course ,  on_delete=models.CASCADE)
    password = models.CharField( max_length=150)


class UnitsDone(models.Model):
    no_of_units = models.IntegerField()
    student = models.ForeignKey(Student ,  on_delete=models.CASCADE)


class Results(models.Model):
    student = models.ForeignKey(Student ,  on_delete=models.CASCADE)
    marks = models.IntegerField()
     





    

# Create your models here.
