from django.urls import path
from .views import get_stud
from .views import create_stud
urlpatterns=[
    path('',get_stud),
    path('create/',create_stud),
    ]