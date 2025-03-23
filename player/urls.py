from django.urls import path
from . import views

urlpatterns = [   
path('hitman/', views.rohit, name='hitman'),
]