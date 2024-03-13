from django.contrib import admin


from .models import School, Department, Course, Student, UnitsDone, Results

admin.site.register(School)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(UnitsDone)
admin.site.register(Results)


# Register your models here.
