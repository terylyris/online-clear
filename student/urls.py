from django.urls import path
from .views import check_units,check_passmark


urlpatterns = [
    path('unitsdone/<str:id>',check_units,name="check-units"),
    path("checkmarks/<str:id>",check_passmark,name="check-passmark"),
]

