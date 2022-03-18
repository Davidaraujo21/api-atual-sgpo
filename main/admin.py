from django.contrib import admin

from .models import Componente, MacroProcesso, Processo, Direcionador, Parte, Entrada, Saida, Ferramenta, Cliente, TiposUsuario, UsuarioInstitucional, UsuarioTematico

modelos = [Componente, MacroProcesso, Processo, Entrada, Saida,
Parte, Direcionador, Ferramenta, Cliente, TiposUsuario, UsuarioInstitucional, UsuarioTematico
]

admin.site.register(modelos)

