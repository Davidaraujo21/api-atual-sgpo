from django.contrib import admin

from .models import Componente, MacroProcesso, Processo, Direcionador, Parte, EntradaSaida, Ferramenta

admin.site.register(Componente)
admin.site.register(MacroProcesso)
admin.site.register(Processo)
admin.site.register(EntradaSaida)
admin.site.register(Parte)
admin.site.register(Direcionador)
admin.site.register(Ferramenta)

