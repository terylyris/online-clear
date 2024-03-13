from django.db import models


class School(models.Model):
    name = models.CharField( max_length=150, unique =   True)

    def __str__(self) -> str:
        return self.name


class Department(models.Model):
     name = models.CharField( max_length=150, unique = True)
     school = models.ForeignKey(School ,  on_delete=models.CASCADE)

     def __str__(self) -> str:
        return self.name


class Course(models.Model):
     name = models.CharField( max_length=150, unique = True)
     department =models.ForeignKey(Department ,  on_delete=models.CASCADE)
     unitsdone = models.IntegerField()

     def __str__(self) -> str:
        return self.name


class Student(models.Model):
    regNo = models.CharField( max_length=150, unique = True)
    name = models.CharField( max_length=150 )
    course = models.ForeignKey(Course ,  on_delete=models.CASCADE)
    password = models.CharField( max_length=150)

    def __str__(self) -> str:
        return self.name


class UnitsDone(models.Model):
    no_of_units = models.IntegerField()
    student = models.ForeignKey(Student ,  on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.student.name


class Results(models.Model):
    student = models.ForeignKey(Student ,  on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self) -> str:
        return self.student.name
     





    

# Create your models here.
