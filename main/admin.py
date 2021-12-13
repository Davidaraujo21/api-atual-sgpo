from django.contrib import admin

from .models import Componente, MacroProcesso, Processo, Direcionador, Parte, Entrada, Saida, Ferramenta, Cliente

modelos = [Componente, MacroProcesso, Processo, Entrada, Saida,
Parte, Direcionador, Ferramenta, Cliente
]

admin.site.register(modelos)

