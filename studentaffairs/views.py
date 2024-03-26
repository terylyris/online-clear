from django.shortcuts import render
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


from .models import Student,Disciplinary, Activity,Hostel,Games,Damages
from .serializers import ActivitySerializer

@api_view()
def disciplinary_records(request,id):
    case = Disciplinary.objects.filter(student__pk = id)
    student = Student.objects.get(pk=id)
    unresolved = 0
    for c in case:
        if not c.resolved:
            uresolved += 1
        else:
            continue

    print(unresolved)
    if unresolved  > 0:
        return Response({"clear":False})
    else:
        return Response({"clear":True})


@api_view()
def activity_done(req,id):
    activities_done =Activity.objects.filter(student__pk = id)
    serializer = ActivitySerializer(activities_done,many=True)
    return Response(serializer.data)


@api_view()
def damagescaused(request,id):
    damages = Damages.objects.filter(student__pk = id).filter(repaired=False).count()   
    if damages>0:
        return Response({"clear":False})
    else:
        return Response({"clear":True})
    


