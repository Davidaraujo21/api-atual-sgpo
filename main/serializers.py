from .models import Componente,MacroProcesso,Parte,Direcionador,EntradaSaida,Ferramenta,Processo
from rest_framework import serializers


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

class EntradaSaidaSerializer(serializers.ModelSerializer):

    class Meta:

        model = EntradaSaida
        fields = '__all__'

class FerramentaSerializer(serializers.ModelSerializer):

    class Meta:

        model = Ferramenta
        fields = '__all__'


class ProcessoReadSerializer(serializers.ModelSerializer):

    macroProcesso_primario = MacroprocessoReadSerializer()
    macroProcessos_vinculados = MacroprocessoReadSerializer(many=True)
    parte = ParteSerializer(many=True)
    direcionador = DirecionadorSerializer(many=True)
    ferramenta = FerramentaSerializer(many=True)

    class Meta:
        model = Processo
        fields = '__all__'
        read_only_fields = ['__all__']


class ProcessoWriteSerializer(serializers.ModelSerializer):

    class Meta:

        model = Processo
        fields = '__all__'
        



