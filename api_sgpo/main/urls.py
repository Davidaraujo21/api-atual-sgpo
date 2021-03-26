from django.urls import path
from . import views


urlpatterns = [
	path('', views.api_root),
	path('componentes/', views.ComponenteList.as_view(), name='componente-list'),
	path('componentes/<int:pk>/', views.ComponenteDetail.as_view(), name='componente-detail'),

	path('macroprocessos/', views.MacroprocessoList.as_view(), name='macroprocesso-list'),
	path('macroprocessos/<int:pk>/', views.MacroProcessoDetail.as_view(), name='macroprocesso-detail'),

	path('partes/', views.ParteList.as_view(), name='partes-list'),
	path('partes/<int:pk>/', views.ParteDetail.as_view(), name='parte-detail'),

	path('direcionadores/', views.DirecionadorList.as_view(), name='direcionadores-list'),
	path('direcionadores/<int:pk>/', views.DirecionadorDetail.as_view(), name='direcionador-detail'),

	path('entradas-saidas/', views.EntradaSaidaList.as_view(), name='entradasaida-list'),
	path('entrada-saidas/<int:pk>/', views.EntradaSaidaDetail.as_view(), name='entradasaida-detail'),

	path('ferramentas/', views.FerramentaList.as_view(), name='ferramentas-list'),
	path('ferramentas/<int:pk>/', views.FerramentaDetail.as_view(), name='ferramenta-detail'),

	path('processos/', views.ProcessoList.as_view(), name='processos-list'),
	path('processos/<int:pk>/', views.ProcessoDetail.as_view(), name='processo-detail'),
]