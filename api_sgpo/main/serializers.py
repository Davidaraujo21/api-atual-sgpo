from .models import Componente,MacroProcesso,Parte,Direcionador,EntradaSaida,Ferramenta,Processo
from rest_framework import serializers


class ComponenteSerializer(serializers.ModelSerializer):

    class Meta:

        model = Componente
        fields = '__all__'


class MacroprocessoSerializer(serializers.ModelSerializer):
    componentes_vinculados = ComponenteSerializer(many=True)
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


class ProcessoSerializer(serializers.ModelSerializer):
    # Está aninhando a entidade relacionada dentro do pai
    # O aninhamento está causando problemas no put
    macroProcesso_primario = MacroprocessoSerializer()
    macroProcessos_vinculados =  MacroprocessoSerializer(many=True)
    parte = ParteSerializer(many=True)
    direcionador = DirecionadorSerializer(many=True)
    entradaSaida = EntradaSaidaSerializer(many=True)
    ferramenta = FerramentaSerializer(many=True)
    class Meta:

        model = Processo
        fields = '__all__'
        



