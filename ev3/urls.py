from django.urls import path
from . import views

urlpatterns = [
	path('', views.ev3, name = 'ev3'),
]