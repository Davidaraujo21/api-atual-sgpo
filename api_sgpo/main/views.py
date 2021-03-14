from django.shortcuts import render
from .models import Componente,Macroprocesso,Parte,Direcionador,EntradaSaida,Ferramenta,Processo
from rest_framework import generics

class ComponenteList(generics.ListCreateAPIView):
	queryset = Componente.objects.all()
	serializer_class = ""

class ComponenteDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Componente.objects.all()
	serializer_class = ""

class MacroprocessoList(generics.ListCreateAPIView):
	queryset = Macroprocesso.objects.all()
	serializer_class = ""

class MacroProcessoDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Macroprocesso.objects.all()
	serializer_class = ""

class ParteList(generics.ListCreateAPIView):
	queryset = Parte.objects.all()
	serializer_class = ""

class ParteDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Parte.objects.all()
	serializer_class = ""

class DirecionadorList(generics.ListCreateAPIView):
	queryset = Direcionador.objects.all();
	serializer_class = ""

class DirecionadorDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Direcionador.objects.all()
	serializer_class = ""

class EntradaSaidaList(generics.ListCreateAPIView):
	queryset = EntradaSaida.objects.all()
	serializer_class = ""

class EntradaSaidaDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = EntradaSaida.objects.all()
	serializer_class = ""

class FerramentaList(generics.ListCreateAPIView):
	queryset = Ferramenta.objects.all()
	serializer_class = ""

class FerramentaDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Ferramenta.objects.all()
	serializer_class = ""

class ProcessoList(generics.ListCreateAPIView):
	queryset = Processo.objects.all()
	serializer_class = ""

class ProcessoDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Processo.objects.all()
	serializer_class = ""


