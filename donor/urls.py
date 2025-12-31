from django.urls import path
from .views import donor_home

urlpatterns = [
    path('', donor_home, name='donor_home'),
]
