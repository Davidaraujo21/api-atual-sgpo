from .models import Componente,MacroProcesso,Parte,Direcionador,Entrada, Saida,Ferramenta,Processo, Cliente, UsuarioInstitucional, UsuarioTematico
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User


class ComponenteSerializer(serializers.ModelSerializer):

    class Meta:

        model = Componente
        fields = '__all__'


class MacroprocessoReadSerializer(serializers.ModelSerializer):

    componente_primario = ComponenteSerializer()
    componentes_vinculados = ComponenteSerializer(many=True)

    class Meta:
        model = MacroProcesso
        fields = '__all__'
        read_only_fields = ['__all__']

class MacroprocessoWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = MacroProcesso
        fields = '__all__'


class ParteSerializer(serializers.ModelSerializer):

    class Meta:

        model = Parte
        fields = '__all__'


class DirecionadorSerializer(serializers.ModelSerializer):

    class Meta:

        model = Direcionador
        fields = '__all__'

class EntradaSerializer(serializers.ModelSerializer):

    class Meta:

        model = Entrada
        fields = '__all__'

class SaidaSerializer(serializers.ModelSerializer):

    class Meta:

        model = Saida
        fields = '__all__'

class FerramentaSerializer(serializers.ModelSerializer):

    class Meta:

        model = Ferramenta
        fields = '__all__'


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Cliente
        fields = '__all__'

class ProcessoReadSerializer(serializers.ModelSerializer):

    macroProcesso_primario = MacroprocessoReadSerializer()
    macroProcessos_vinculados = MacroprocessoReadSerializer(many=True)
    parte = ParteSerializer(many=True)
    direcionador = DirecionadorSerializer(many=True)
    ferramenta = FerramentaSerializer(many=True)
    clientes = ClienteSerializer(many=True)
    entradas = EntradaSerializer(many=True)
    saidas = SaidaSerializer(many=True)

    class Meta:
        model = Processo
        fields = '__all__'
        read_only_fields = ['__all__']


class ProcessoWriteSerializer(serializers.ModelSerializer):

    class Meta:

        model = Processo
        fields = '__all__'
        

def get_usuario_tipo(usuario):
    try:
        institucional = UsuarioInstitucional.objects.filter(usuario=usuario).get()
        return 1
    except:
        pass
    try:
        tematico = UsuarioTematico.objects.filter(usuario=usuario).get()
        return 2
    except:
        pass
    return 0

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        usuario = User.objects.filter(username=user.username, password=user.password).get()
        tipo_usuario = get_usuario_tipo(usuario)
        token['username'] = user.username
        token['tipo_usuario'] = tipo_usuario
        return token

