from django.db import models
from django.core.validators import FileExtensionValidator

class Componente(models.Model):
    nome_componente = models.CharField(max_length = 200)
    objetivo = models.CharField(max_length = 200)
    codigo = models.CharField(max_length=5, default = '', unique = True)
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
    codigo = models.CharField(max_length=5, default = '', unique = True)
    componente_primario = models.ForeignKey('Componente', on_delete=models.CASCADE)
    componentes_vinculados = models.ManyToManyField('Componente', related_name='componentesVincAcess', blank=True)
    def __str__(self):
        return self.nome_macroprocesso

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

class Direcionador(models.Model):
    orgao = models.CharField(max_length = 200)
    numero = models.CharField(max_length = 200)
    data = models.DateField()
    descricao = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
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
        return self.orgao

class Entrada(models.Model):
    descricao = models.TextField()
    arquivo = models.FileField(null=True, upload_to='arquivos/%Y/%m/%d/', validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    def __str__(self):
        return self.descricao

class Saida(models.Model):
    descricao = models.TextField()
    TIPO_CHOICES = (
        ('Produto', 'Produto'),
        ('Serviço', 'Serviço')
    )
    tipoSaida = models.CharField(max_length = 7, choices = TIPO_CHOICES)
    def __str__(self):
        return self.descricao

class Ferramenta(models.Model):
    descricao = models.TextField()
    def __str__(self):
        return self.descricao

class Cliente(models.Model):
    nome = models.CharField(max_length = 200)
    TIPO_CHOICES = (
        ('Pessoa', 'Pessoa'),
        ('Unidade', 'Unidade')
    )
    tipoCliente = models.CharField(max_length=7, choices=TIPO_CHOICES)
    def __str__(self):
        return self.nome

#------------------------------------------------------------------------------------------
# Classe referente a identificação do processo
#------------------------------------------------------------------------------------------
class Processo(models.Model):
    nome_processo = models.CharField(max_length = 200)
    gestorPrincipal = models.CharField(max_length = 200)
    proprietario = models.CharField(max_length = 200)
    fronteiraDe = models.CharField(max_length = 200)
    fronteiraAte = models.CharField(max_length = 200)
    objetivo = models.TextField()
    codigo = models.CharField(max_length=5, default = '', unique = True)
    proad = models.CharField(max_length = 12)
    versaop = models.IntegerField(default = 0)
    data_inicial_versao_processo =  models.DateTimeField(auto_now=True)
    etapas = models.TextField()
    clientes = models.ManyToManyField(Cliente, related_name='cliente', blank=True)
    # RELACIONAMENTOS COM AS DEMAIS CLASSES
    macroProcesso_primario = models.ForeignKey(MacroProcesso,on_delete=models.CASCADE, related_name='macroProcessoPrim')
    macroProcessos_vinculados = models.ManyToManyField(MacroProcesso, related_name='macroProcessoVinc', blank=True)
    parte = models.ManyToManyField(Parte, related_name="processoParte")
    direcionador = models.ManyToManyField(Direcionador, related_name='processoDirecionador')
    entradas = models.ManyToManyField(Entrada, related_name="processoEntradas")
    saidas = models.ManyToManyField(Saida, related_name="processoSaidas")
    ferramenta = models.ManyToManyField(Ferramenta, related_name='processoFerramenta')
    def __str__(self):
        return self.nome_processo



