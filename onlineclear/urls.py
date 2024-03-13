from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('finance/',include("finance.urls")),
    path('library/',include("library.urls")),
    path('student/',include("student.urls")),
    path('studentaffairs/',include("studentaffairs.urls"))
    
]
