from django.shortcuts import render
from .models import Componente,MacroProcesso,Parte,Direcionador,EntradaSaida,Ferramenta,Processo
from .serializers import ComponenteSerializer, MacroprocessoSerializer, ParteSerializer, DirecionadorSerializer, EntradaSaidaSerializer, FerramentaSerializer, ProcessoSerializer
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from .filtros import ProcessoFilter


class ComponenteViewSet(viewsets.ModelViewSet):
	queryset = Componente.objects.all()
	serializer_class = ComponenteSerializer

class MacroProcessoViewSet(viewsets.ModelViewSet):
	queryset = MacroProcesso.objects.all()
	serializer_class = MacroprocessoSerializer

class ParteViewSet(viewsets.ModelViewSet):
	queryset = Parte.objects.all()
	serializer_class = ParteSerializer

class DirecionadorViewSet(viewsets.ModelViewSet):
	queryset = Direcionador.objects.all()
	serializer_class = DirecionadorSerializer

class EntradaSaidaViewSet(viewsets.ModelViewSet):
	queryset = EntradaSaida.objects.all()
	serializer_class = EntradaSaidaSerializer

class FerramentaViewSet(viewsets.ModelViewSet):
	queryset = Ferramenta.objects.all()
	serializer_class = FerramentaSerializer

class ProcessoViewSet(viewsets.ModelViewSet):
	queryset = Processo.objects.all()
	serializer_class = ProcessoSerializer
	filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
	filterset_class = ProcessoFilter
	ordering_fields = ['nome_processo', 'codigo', 'data_inicial_versao_processo']
	pagination_class = LimitOffsetPagination


