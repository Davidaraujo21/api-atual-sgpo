from django.urls import path
from . import views

urlpatterns = [
	path('componentes/', views.ComponenteList.as_view(), name='componente-list'),
	path('componente/<int:codigo>/', views.ComponenteDetail.as_view(), name='componente-detail'),

	path('macroprocessos/', views.MacroprocessoList.as_view(), name='macroprocesso-list'),
	path('macroprocesso/<int:codigo>/', views.MacroProcessoDetail.as_view(), name='macroprocesso-detail'),

	path('partes/', views.ParteList.as_view(), name='partes-list'),
	path('parte/<int:id>/', views.ParteDetail.as_view(), name='parte-detail'),

	path('direcionadores/', views.DirecionadorList.as_view(), name='direcionadores-list'),
	path('direcionador/<int:numero>/', views.DirecionadorDetail.as_view(), name='direcionador-detail'),

	path('entradas-saidas/', views.EntradaSaidaList.as_view(), name='entradasaida-list'),
	path('entrada-saida/<int:id>/', views.EntradaSaidaDetail.as_view(), name='entradasaida-detail'),

	path('ferramentas/', views.FerramentaList.as_view(), name='ferramentas-list'),
	path('ferramenta/<int:id>/', views.FerramentaDetail.as_view(), name='ferramenta-detail'),

	path('processos/', views.ProcessoList.as_view(), name='processos-list'),
	path('processo/<int:codigo>/', views.ProcessoDetail.as_view(), name='processo-detail'),
]