from django.contrib import admin

from .models import Library

class LibraryAdmin(admin.ModelAdmin):
    list_display = ['bookborrowed','student','returned']

admin.site.register(Library,LibraryAdmin)

# Register your models here.
