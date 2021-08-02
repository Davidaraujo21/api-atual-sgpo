from .models import Componente,MacroProcesso,Parte,Direcionador,EntradaSaida,Ferramenta,Processo
from rest_framework import serializers
from django.contrib.auth import get_user_model


class ComponenteSerializer(serializers.ModelSerializer):

    class Meta:

        model = Componente
        fields = '__all__'


class MacroprocessoSerializer(serializers.ModelSerializer):
    #por padrão é read-only
    componentes_vinculados = ComponenteSerializer(many=True, read_only=True)
    
    class Meta:
        model = MacroProcesso
        fields = '__all__'

    #criar método create para permirtir que possa realizar a escritar de serializers aninhados
    # def create(self, validated_data):
    #     comps = validated_data.pop('componentes_vinculados')
    #     macroprocesso = MacroProcesso.objects.create(**validated_data)
    #     for comp in comps:
    #         Componente.objects.create(macroprocesso=macroprocesso, **comp)
    #     return macroprocesso
    

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
        



