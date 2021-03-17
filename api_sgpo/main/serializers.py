from .models import Componente,Macroprocesso,Parte,Direcionador,EntradaSaida,Ferramenta,Processo
from rest_framework import serializers

class ComponenteSerializer(serializers.ModelSerializer):

    class Meta:

        model = Componente
        fields = '__all__'


class MacroprocessoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Macroprocesso
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

    class Meta:

        model = Processo
        fields = '__all__'




