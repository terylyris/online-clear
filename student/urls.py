from django.urls import path
from .views import check_units,check_passmark,login


urlpatterns = [
    path('unitsdone/<str:id>',check_units,name="check-units"),
    path("checkmarks/<str:id>",check_passmark,name="check-passmark"),
    path('login/',login,name='login')
]

