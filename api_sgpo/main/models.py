from django.db import models

class Componente(models.Model):
    nome_componente = models.CharField(max_length = 200)
    objetivo = models.CharField(max_length = 200)
    codigo = models.CharField(max_length=64, default = '', unique = True)
    TIPO_CHOICES = (
        ('finalistico', 'finalistico'),
        ('direcionador', 'direcionador'),
        ('apoio', 'apoio'),
        )
    tipo = models.CharField(max_length = 200, choices = TIPO_CHOICES)
    def __str__(self):
        return self.nome_componente

class MacroProcesso(models.Model):
    nome_macroprocesso = models.CharField(max_length = 200)
    objetivo = models.CharField(max_length = 200)
    codigo = models.CharField(max_length=64, default = '', unique = True)
    componente_primario = models.ForeignKey('Componente', on_delete=models.CASCADE)
    componentes_vinculados = models.ManyToManyField('Componente', blank=True, related_name='componentesVincAcess')
    def __str__(self):
        return self.nome_macroprocesso

#------------------------------------------------------------------------------------------
#  classe referente a PARTES INTERESSADAS
#------------------------------------------------------------------------------------------
class Parte(models.Model):
    nomeParte = models.CharField(max_length = 200)
    sigla = models.CharField(max_length = 20)
    TIPO_CHOICES = (
        ('Pe', 'Pessoa'),
        ('C', 'Cargo'),
        ('U', 'Unidade'),
        ('S', 'Setor'),
        ('O', 'Órgão'),
        ('C', 'Comitê'),
        ('Pa', 'Papel'),
        ('G', 'Grupo'),
        )
    tipoParte = models.CharField(max_length = 2, choices = TIPO_CHOICES)

    def __str__(self):
        return self.nomeParte

#------------------------------------------------------------------------------------------
# Classe referente aos Direcionadores
#------------------------------------------------------------------------------------------
class Direcionador(models.Model):
    Orgao = models.CharField(max_length = 200)
    numero = models.CharField(max_length = 200)
    ano = models.DateField()
    descricao = models.TextField()
    url = models.URLField()
    TIPO_CHOICES = (
        ('L', 'Lei'),
        ('D', 'Decreto'),
        ('R', 'Resolução'),
        ('A', 'Ato'),
        ('Po', 'Portaria'),
        ('M', 'Manual'),
      )
    tipoParte = models.CharField(max_length = 2, choices = TIPO_CHOICES)
    def __str__(self):
        return self.Orgao

#------------------------------------------------------------------------------------------
#Classes referente a entradas e saídas
#------------------------------------------------------------------------------------------
class EntradaSaida(models.Model):
    descricao = models.TextField()
    def __str__(self):
        return self.descricao

#------------------------------------------------------------------------------------------
# Classes referentes as ferramentas
#------------------------------------------------------------------------------------------
class Ferramenta(models.Model):
    descricao = models.TextField()
    def __str__(self):
        return self.descricao

#------------------------------------------------------------------------------------------
# Classe referente a identificação do processo
#------------------------------------------------------------------------------------------
class Processo(models.Model):
    nome_processo = models.CharField(max_length = 200)
    gestorPrincipal = models.CharField(max_length = 200, null=True, blank=True)
    proprietario = models.CharField(max_length = 200, null=True, blank=True)
    fronteiraDe = models.CharField(max_length = 200)
    fronteirAte = models.CharField(max_length = 200)
    objetivo = models.CharField(max_length = 200)
    codigo = models.CharField(max_length=64, default = '', unique = True)
    proad = models.CharField(max_length = 12, null=True, blank=True)
    versaop = models.IntegerField(default = 0)
    data_inicial_versao_processo =  models.DateTimeField('data inicial de publicacao do processo')

    # RELACIONAMENTOS COM AS DEMAIS CLASSES
    macroProcesso_primario = models.ForeignKey(MacroProcesso,on_delete=models.CASCADE)
    macroProcessos_vinculados = models.ManyToManyField(MacroProcesso, blank=True, related_name='macroProcesVincAcess')
    parte = models.ManyToManyField(Parte)
    direcionador = models.ManyToManyField(Direcionador)
    entradaSaida = models.ManyToManyField(EntradaSaida)
    ferramenta = models.ManyToManyField(Ferramenta)
    def __str__(self):
        return self.nome_processo



