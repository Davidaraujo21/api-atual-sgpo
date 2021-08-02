from django.contrib import admin

from .models import Componente, MacroProcesso, Processo, Direcionador, Parte, EntradaSaida, Ferramenta

modelos = [Componente, MacroProcesso, Processo, EntradaSaida,
Parte, Direcionador, Ferramenta
]

admin.site.register(modelos)

