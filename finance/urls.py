from django.urls import path


from .views import check_balance

urlpatterns = [
    path('check/<str:reg_no>',check_balance,name="check-balance"),
]
