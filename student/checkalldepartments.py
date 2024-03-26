from .models import Results,UnitsDone,Course,Student
from library.models import Library
from finance.models import Finance
from studentaffairs.models import Damages,Disciplinary


def checkFaculty(id):
    results = Results.objects.filter(student__pk = id)
    failedunits = 0
    complete_units = False
    passed = False
    for result in results:
        if result.marks > 39:
            continue
        elif result.marks < 40:
            failedunits += 1
    if failedunits>0:
        passed = False
    else:
        passed = True
    
    units_done = UnitsDone.objects.get(student__pk = id)
    student = Student.objects.get(pk=id)
    expected_units = Course.objects.get(name = student.course.name)
    if units_done.no_of_units == expected_units.unitsdone:
        complete_units = True
    else:
        complete_units = False

    if complete_units and passed:
        return True
    return False

def checkLibrary(id):
    returned = Library.objects.get(student__pk = id)
    if returned.returned:
        return True
    else:
        return False
    
def checkFinance(id):
    balance = Finance.objects.get(student__pk = id)
    if balance.balance > 0:
        return False
    else:
        return True
    
def checkStudentAffairs(id):
    case = Disciplinary.objects.filter(student__pk = id)
    student = Student.objects.get(pk=id)
    disciplinary = False
    resolved_damages = False
    unresolved = 0
    for c in case:
        if not c.resolved:
            uresolved += 1
        else:
            continue

    print(unresolved)
    if unresolved  > 0:
        disciplinary =  False
    else:
        disciplinary = True

    damages = Damages.objects.filter(student__pk = id).filter(repaired=False).count()   
    if damages>0:
        resolved_damages = False 
    else:
        resolved_damages = True

    if resolved_damages and disciplinary:
        return True
    else:
        return False



        

    
    
