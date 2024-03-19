from django.contrib import admin

from .models import Activity, Disciplinary, Hostel, Damages, Games

class ActivityAdmin(admin.ModelAdmin):
    list_display = ['activityname','student',]
class DisciplinaryAdmin(admin.ModelAdmin):
    list_display = ['student','case','resolved']
class DamagesAdmin(admin.ModelAdmin):
    list_display = ['student','damagecaused','repaired']
class HostelAdmin(admin.ModelAdmin):
    list_display = ['student','checkindate','checkoutdate', 'hostelname']
class GamesAdmin(admin.ModelAdmin):
    list_display = ['student','activity',]


admin.site.register(Activity, ActivityAdmin)
admin.site.register(Disciplinary, DisciplinaryAdmin)
admin.site.register(Hostel,HostelAdmin)
admin.site.register(Damages,DamagesAdmin)
admin.site.register(Games, GamesAdmin)


# Register your models here.
