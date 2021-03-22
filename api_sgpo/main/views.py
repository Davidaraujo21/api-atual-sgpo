from django.shortcuts import render
from .models import Componente,MacroProcesso,Parte,Direcionador,EntradaSaida,Ferramenta,Processo
from .serializers import ComponenteSerializer, MacroprocessoSerializer, ParteSerializer, DirecionadorSerializer, EntradaSaidaSerializer, FerramentaSerializer, ProcessoSerializer
from rest_framework import generics
from rest_framework import filters
from .pagination import CustomPagination
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django_filters.rest_framework import DjangoFilterBackend
from .filtros import ProcessoFilter


@api_view(['GET'])
def api_root(request, format=None):
	return Response({
			'processos': reverse('processos-list', request=request, format=format),
			'macroprocessos': reverse('macroprocesso-list', request=request, format=format),
			'componentes': reverse('componente-list', request=request, format=format),
			'partes': reverse('partes-list', request=request, format=format),
			'direcionadores': reverse('direcionadores-list', request=request, format=format),
			'entradas-saidas': reverse('entradasaida-list', request=request, format=format),
			'ferramentas': reverse('ferramentas-list', request=request, format=format)
	})

class ComponenteList(generics.ListCreateAPIView):
	queryset = Componente.objects.all()
	serializer_class = ComponenteSerializer

class ComponenteDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Componente.objects.all()
	serializer_class = ComponenteSerializer

class MacroprocessoList(generics.ListCreateAPIView):
	queryset = MacroProcesso.objects.all()
	serializer_class = MacroprocessoSerializer

class MacroProcessoDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = MacroProcesso.objects.all()
	serializer_class = MacroprocessoSerializer

class ParteList(generics.ListCreateAPIView):
	queryset = Parte.objects.all()
	serializer_class = ParteSerializer

class ParteDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Parte.objects.all()
	serializer_class = ParteSerializer

class DirecionadorList(generics.ListCreateAPIView):
	queryset = Direcionador.objects.all()
	serializer_class = DirecionadorSerializer

class DirecionadorDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Direcionador.objects.all()
	serializer_class = DirecionadorSerializer

class EntradaSaidaList(generics.ListCreateAPIView):
	queryset = EntradaSaida.objects.all()
	serializer_class = EntradaSaidaSerializer

class EntradaSaidaDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = EntradaSaida.objects.all()
	serializer_class = EntradaSaidaSerializer

class FerramentaList(generics.ListCreateAPIView):
	queryset = Ferramenta.objects.all()
	serializer_class = FerramentaSerializer

class FerramentaDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Ferramenta.objects.all()
	serializer_class = FerramentaSerializer

class ProcessoList(generics.ListCreateAPIView):
	queryset = Processo.objects.all()
	serializer_class = ProcessoSerializer
	filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
	filterset_class = ProcessoFilter
	ordering_fields = ['nome_processo', 'codigo', 'data_inicial_versao_processo']
	pagination_class = CustomPagination

class ProcessoDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Processo.objects.all()
	serializer_class = ProcessoSerializer


