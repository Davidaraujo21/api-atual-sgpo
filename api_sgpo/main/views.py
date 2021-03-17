from django.shortcuts import render
from .models import Componente,MacroProcesso,Parte,Direcionador,EntradaSaida,Ferramenta,Processo
from rest_framework import generics

class ComponenteList(generics.ListCreateAPIView):
	queryset = Componente.objects.all()
	serializer_class = "ComponenteSerializer"

class ComponenteDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Componente.objects.all()
	serializer_class = "ComponenteSerializer"

class MacroprocessoList(generics.ListCreateAPIView):
	queryset = MacroProcesso.objects.all()
	serializer_class = "MacroprocessoSerializer"

class MacroProcessoDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = MacroProcesso.objects.all()
	serializer_class = "MacroprocessoSerializer"

class ParteList(generics.ListCreateAPIView):
	queryset = Parte.objects.all()
	serializer_class = "ParteSerializer"

class ParteDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Parte.objects.all()
	serializer_class = "ParteSerializer"

class DirecionadorList(generics.ListCreateAPIView):
	queryset = Direcionador.objects.all()
	serializer_class = "DirecionadorSerializer"

class DirecionadorDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Direcionador.objects.all()
	serializer_class = "DirecionadorSerializer"

class EntradaSaidaList(generics.ListCreateAPIView):
	queryset = EntradaSaida.objects.all()
	serializer_class = "EntradaSaidaSerializer"

class EntradaSaidaDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = EntradaSaida.objects.all()
	serializer_class = "EntradaSaidaSerializer"

class FerramentaList(generics.ListCreateAPIView):
	queryset = Ferramenta.objects.all()
	serializer_class = "FerramentaSerializer"

class FerramentaDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Ferramenta.objects.all()
	serializer_class = "FerramentaSerializer"

class ProcessoList(generics.ListCreateAPIView):
	queryset = Processo.objects.all()
	serializer_class = "ProcessoSerializer"

class ProcessoDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Processo.objects.all()
	serializer_class = "ProcessoSerializer"


