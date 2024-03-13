from django.urls import path
from .views import book_returned


urlpatterns = [
    path('returned/<str:reg_no>/',book_returned,name="book-returned"),
]


