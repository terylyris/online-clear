from django.urls import path
from .views import disciplinary_records
from .views import activity_done
from .views import damagescaused


urlpatterns = [
    path('disciplinary/<str:reg_no>/',disciplinary_records,name="case"),
    path('activities/<str:reg_no>/',activity_done,name="case"),
    path('damages/<str:reg_no>/',damagescaused,name="case"),
]

