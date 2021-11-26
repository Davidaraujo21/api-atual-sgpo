from django_filters import rest_framework as filters
from main.models import Processo, MacroProcesso

class ProcessoFilter(filters.FilterSet):	
	cod_processo = filters.CharFilter(field_name='codigo', lookup_expr='contains')
	macroprocesso = filters.CharFilter(field_name='macroProcesso_primario__nome_macroprocesso', lookup_expr='contains')
	processo_nome = filters.CharFilter(field_name='nome_processo', lookup_expr='contains')
	class Meta:
		model = Processo
		fields = ['cod_processo','processo_nome','macroprocesso', 'proprietario', 'gestorPrincipal']

class MacroProcessoFilter(filters.FilterSet):
	cod_macroprocesso = filters.CharFilter(field_name='codigo', lookup_expr='contains')
	componente = filters.CharFilter(field_name="componente_primario__nome_componente", lookup_expr='contains')

	class Meta:
		model = MacroProcesso
		fields = ['cod_macroprocesso', 'componente']