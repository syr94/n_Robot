from django.urls import path
from . import views

urlpatterns = [
	path('', views.python, name = 'python'),
]