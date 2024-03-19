from django.db import models
from student.models import Student


class Library(models.Model):
  student = models.ForeignKey(Student ,  on_delete=models.CASCADE,null=True)
  bookborrowed =models.CharField( max_length=150, )
  returned = models.BooleanField(default=False)

  def __str__(self):
      return self.bookborrowed
  

# Create your models here.
