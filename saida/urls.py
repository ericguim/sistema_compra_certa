from django.urls import path
from . import views

urlpatterns = [
    path('saida/', views.saida, name='saida'),
]