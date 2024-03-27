from django.contrib import admin




from .models import School, Department, Course, Student, UnitsDone, Results
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['name',]
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name','school',]
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name','department','unitsdone']
class StudentsAdmin(admin.ModelAdmin):
    list_display = ['regNo','name','course']
class UnitsDoneAdmin(admin.ModelAdmin):
    list_display = ['no_of_units','student',]
class ResultsAdmin(admin.ModelAdmin):
    list_display = ['student','marks',]


admin.site.site_title = "Online Clear"
admin.site.index_title = "Online Clear"
admin.site.site_header = "online clear"


admin.site.register(School)
admin.site.register(Department,DepartmentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentsAdmin)
admin.site.register(UnitsDone , UnitsDoneAdmin)
admin.site.register(Results, ResultsAdmin)


# Register your models here.
