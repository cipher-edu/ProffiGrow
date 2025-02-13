from django.urls import path
from .views import *
from django.conf import settings

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]