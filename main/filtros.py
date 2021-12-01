from django_filters import rest_framework as filters
from main.models import Processo, MacroProcesso, Componente

class ProcessoFilter(filters.FilterSet):	
	cod_processo = filters.CharFilter(field_name='codigo', lookup_expr='contains')
	macroprocesso = filters.CharFilter(field_name='macroProcesso_primario__nome_macroprocesso', lookup_expr='contains')
	processo_nome = filters.CharFilter(field_name='nome_processo', lookup_expr='contains')
	componente_primario = filters.CharFilter(field_name='macroProcesso_primario__componente_primario__tipo', lookup_expr='contains')
	
	class Meta:
		model = Processo
		fields = ['cod_processo','processo_nome','macroprocesso', 'proprietario', 'gestorPrincipal', "componente_primario"]

class MacroProcessoFilter(filters.FilterSet):
	cod_macroprocesso = filters.CharFilter(field_name='codigo', lookup_expr='contains')
	componente = filters.CharFilter(field_name="componente_primario__nome_componente", lookup_expr='contains')

	class Meta:
		model = MacroProcesso
		fields = ['cod_macroprocesso', 'componente']

class ComponenteFilter(filters.FilterSet):

	cod_componente = filters.CharFilter(field_name='codigo', lookup_expr='contains')
	tipo_componente = filters.CharFilter(field_name='tipo', lookup_expr='contains')

	class Meta: 
		model = Componente
		fields = ['nome_componente', 'tipo_componente']
