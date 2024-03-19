from django.contrib import admin

from .models import Finance

class FinanceAdmin(admin.ModelAdmin):
    list_display = ['student','balance',]


admin.site.register(Finance, FinanceAdmin)

# Register your models here.
