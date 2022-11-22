from django.urls import path
from . import views

urlpatterns = [
    path('', views.estoque, name='estoque'),
    path('analise/', views.analise, name='analise'),
]