
from django.shortcuts import render
from serializers import LibrarySerializer
from models import Library, Student
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view()
def book_returned (request, reg_no):
  #student = Student.objects.get(regNo=reg_no)
    returned = Library.objects.get(student__regNo = reg_no)
    if returned.returned:
        return Response({"clear":True})
    else:
        return Response({"clear":False})


# Create your views here.
