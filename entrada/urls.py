from django.urls import path
from . import views

urlpatterns = [
    path('entrada/', views.entrada, name='entrada'),
]