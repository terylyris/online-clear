from django.shortcuts import render
from .serializers import FinanceSerializer
from .models import Finance, Student
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view()
def check_balance(request, reg_no):
  #student = Student.objects.get(regNo=reg_no)
  balance = Finance.objects.get(student__pk = reg_no)
  if balance.balance > 0:
    return Response({"clear":False})
  else:
     return Response({"clear":True})

    

# Create your views here.
