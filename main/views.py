from django.shortcuts import render
from .models import Componente,MacroProcesso,Parte,Direcionador,EntradaSaida,Ferramenta,Processo
from .serializers import ComponenteSerializer, MacroprocessoReadSerializer, MacroprocessoWriteSerializer, ParteSerializer, DirecionadorSerializer, EntradaSaidaSerializer, FerramentaSerializer, ProcessoReadSerializer, ProcessoWriteSerializer
from rest_framework import filters, viewsets, permissions
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from .mixins.read_e_write_serializers import ReadWriteSerializerMixin
from .filtros import ProcessoFilter, MacroProcessoFilter


class ComponenteViewSet(viewsets.ModelViewSet):
	queryset = Componente.objects.all()
	serializer_class = ComponenteSerializer
	pagination_class = LimitOffsetPagination

class MacroProcessoViewSet(ReadWriteSerializerMixin ,viewsets.ModelViewSet):
	queryset = MacroProcesso.objects.all()
	read_serializer_class = MacroprocessoReadSerializer
	write_serializer_class = MacroprocessoWriteSerializer
	filterset_class = MacroProcessoFilter
	ordering_fields = ['nome_macroprocesso', 'codigo']
	pagination_class = LimitOffsetPagination

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

class ProcessoViewSet(ReadWriteSerializerMixin ,viewsets.ModelViewSet):
	queryset = Processo.objects.all()
	read_serializer_class = ProcessoReadSerializer
	write_serializer_class = ProcessoWriteSerializer
	filter_backends = [filters.OrderingFilter]
	filterset_class = ProcessoFilter
	ordering_fields = ['nome_processo', 'codigo', 'data_inicial_versao_processo']
	pagination_class = LimitOffsetPagination


