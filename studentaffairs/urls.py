from django.urls import path
from .views import disciplinary_records
from .views import activity_done
from .views import damagescaused


urlpatterns = [
    path('disciplinary/<str:id>/',disciplinary_records,name="case"),
    path('activities/<str:id>/',activity_done,name="case"),
    path('damages/<str:id>/',damagescaused,name="case"),
]

