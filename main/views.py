from django.shortcuts import render
from .models import Componente,MacroProcesso,Parte,Direcionador,Entrada,Saida,Ferramenta,Processo, Cliente
from .serializers import ComponenteSerializer, MacroprocessoReadSerializer, MacroprocessoWriteSerializer, ParteSerializer, DirecionadorSerializer, EntradaSerializer, SaidaSerializer, FerramentaSerializer, ProcessoReadSerializer, ProcessoWriteSerializer, ClienteSerializer, CustomTokenObtainPairSerializer
from rest_framework import filters, viewsets, permissions
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from .mixins.read_e_write_serializers import ReadWriteSerializerMixin
from .filtros import ProcessoFilter, MacroProcessoFilter, ComponenteFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

class ComponenteViewSet(viewsets.ModelViewSet):
	queryset = Componente.objects.all()
	permission_classes = [IsAuthenticated]
	serializer_class = ComponenteSerializer
	filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
	filterset_class = ComponenteFilter
	pagination_class = LimitOffsetPagination


class MacroProcessoViewSet(ReadWriteSerializerMixin ,viewsets.ModelViewSet):
	queryset = MacroProcesso.objects.all()
	read_serializer_class = MacroprocessoReadSerializer
	write_serializer_class = MacroprocessoWriteSerializer
	permission_classes = [IsAuthenticated]
	filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
	filterset_class = MacroProcessoFilter
	ordering_fields = ['nome_macroprocesso', 'codigo']
	pagination_class = LimitOffsetPagination

class ParteViewSet(viewsets.ModelViewSet):
	queryset = Parte.objects.all()
	permission_classes = [IsAuthenticated]
	serializer_class = ParteSerializer

class DirecionadorViewSet(viewsets.ModelViewSet):
	queryset = Direcionador.objects.all()
	permission_classes = [IsAuthenticated]
	serializer_class = DirecionadorSerializer

class EntradaViewSet(viewsets.ModelViewSet):
	queryset = Entrada.objects.all()
	permission_classes = [IsAuthenticated]
	serializer_class = EntradaSerializer

class SaidaViewSet(viewsets.ModelViewSet):
	queryset = Saida.objects.all()
	permission_classes = [IsAuthenticated]
	serializer_class = SaidaSerializer

class FerramentaViewSet(viewsets.ModelViewSet):
	queryset = Ferramenta.objects.all()
	permission_classes = [IsAuthenticated]
	serializer_class = FerramentaSerializer

class ClienteViewSet(viewsets.ModelViewSet):
	queryset = Cliente.objects.all()
	permission_classes = [IsAuthenticated]
	serializer_class = ClienteSerializer

class ProcessoViewSet(ReadWriteSerializerMixin ,viewsets.ModelViewSet):
	queryset = Processo.objects.prefetch_related("macroProcesso_primario").prefetch_related("macroProcessos_vinculados").prefetch_related("parte").prefetch_related("direcionador").prefetch_related("ferramenta").prefetch_related("clientes").prefetch_related("entradas").prefetch_related("saidas").all()
	read_serializer_class = ProcessoReadSerializer
	write_serializer_class = ProcessoWriteSerializer
	permission_classes = [IsAuthenticated]
	filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
	filterset_class = ProcessoFilter
	ordering_fields = ['nome_processo', 'codigo', 'data_inicial_versao_processo']
	pagination_class = LimitOffsetPagination


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer