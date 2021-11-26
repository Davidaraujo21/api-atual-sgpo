from django.urls import path, include
from rest_framework.routers import DefaultRouter 
from main import views

# Criar uma rota e registrar os viewsets
router = DefaultRouter()
router.register(r'componentes',views.ComponenteViewSet)
router.register(r'macroprocessos', views.MacroProcessoViewSet)
router.register(r'partes', views.ParteViewSet)
router.register(r'direcionadores', views.DirecionadorViewSet)
router.register(r'entradas-saidas', views.EntradaSaidaViewSet)
router.register(r'ferramentas', views.FerramentaViewSet)
router.register(r'processos', views.ProcessoViewSet)


urlpatterns = [
	path('api/', include(router.urls))
]
