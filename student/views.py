from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import StudentSerializer
from rest_framework import status

from .models import Results,UnitsDone,Course,Student
from .checkalldepartments import checkFaculty,checkLibrary,checkFinance,checkStudentAffairs

@api_view()
def checkStatus(req,id):
    faculty = checkFaculty(id)
    library = checkLibrary(id)
    student_affairs = checkStudentAffairs(id)
    finance = checkFinance(id)
    response = {
        "faculty": faculty,
        "library":library,
        "studentaffairs":student_affairs,
        "finance":finance
    }
    return Response(response)
    



@api_view()
def check_passmark(request,id):
    results = Results.objects.filter(student__pk = id)
    failedunits = 0
    for result in results:
        if result.marks > 39:
            continue
        elif result.marks < 40:
            failedunits += 1
    if failedunits>0:
        return Response({"clear":False})
    return Response({"clear":True})

@api_view()
def check_units(req,id):
    units_done = UnitsDone.objects.get(student__pk = id)
    student = Student.objects.get(pk=id)
    expected_units = Course.objects.get(name = student.course.name)
    if units_done.no_of_units == expected_units.unitsdone:
        return Response({"clear":True})
    else:
        return Response({"clear":False})

@api_view(['POST'])
def login(request):
    regno = request.POST.get('regno')
    password = request.POST.get('password')
    print(request.POST)
    print(password)
    try:
        student = Student.objects.get(regNo=regno)
        if student.password == password:
            serializer = StudentSerializer(student)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response({"message":"Wrong PAssword"},status=status.HTTP_401_UNAUTHORIZED)
    except Student.DoesNotExist:
        return Response({'message':"Wrong Registration number"},status=status.HTTP_401_UNAUTHORIZED)



