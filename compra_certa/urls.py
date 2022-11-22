from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'produtos', views.ProdutoViewSet)
router.register(r'fornecedores', views.FornecedorViewSet)
router.register(r'entradas', views.EntradaViewSet)
router.register(r'saidas', views.SaidaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('estoque.urls')),
    path('entrada/', include('entrada.urls')),
    path('saida/', include('saida.urls')),
    path('accounts/', include('accounts.urls')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
