from django.urls import path
from .views import showblog

urlpatterns = [
    path('',showblog, name = 'showblog'),
]