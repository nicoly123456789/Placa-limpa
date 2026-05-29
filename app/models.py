from django.db import models

class Rua(models.Model):
    nome = models.CharField(max_length=120)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Rua"
        verbose_name_plural = "Ruas"

class Policial(models.Model):
    matricula = models.CharField(max_length=100)
    setor = models.CharField(max_length=300)

    def __str__(self):
        return self.matricula

    class Meta:
        verbose_name = "Policial"
        verbose_name_plural = "Policiais"

class Evidencia(models.Model):
    descricao = models.CharField(max_length=500)
    tipoarquivo = models.CharField(max_length=1000)
    dataUpload = models.DateField()

    def __str__(self):
        return self.descricao
    

    class Meta:
        verbose_name = "Evidencia"
        verbose_name_plural = "Evidencias"

class TipoInfracao(models.Model):
    nome = models.CharField(max_length=100)
    gravidade = models.CharField(max_length=100)
    descricao = models.CharField(max_length=300)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "tipoInfracao"
        verbose_name_plural = "tipoInfracoes"

class Usuario(models.Model):
    nome = models.CharField(max_length=45)
    cpf = models.CharField(max_length=12, unique=True)
    email = models.EmailField()
    rua = models.ForeignKey(Rua, on_delete=models.CASCADE)
    n_casa = models.CharField(max_length=10)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

class Denuncia(models.Model):
    descricao = models.CharField(max_length=500)
    rua = models.ForeignKey(Rua, on_delete=models.CASCADE)
    data = models.DateField()
    infrator = models.CharField(max_length=100)
    denunciante = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    evidencia = models.ForeignKey(Evidencia, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Denuncia"
        verbose_name_plural = "Denuncias"

class Penalidade(models.Model):
    infrator = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    policial = models.ForeignKey(Policial, on_delete=models.CASCADE)
    idade_infrator = models.CharField(max_length=2)
    responsavel = models.CharField(max_length=50)
    tipo_infracao = models.ForeignKey(TipoInfracao, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.infrator} - {self.tipo_infracao}"

    class Meta:
        verbose_name = "Penalidade"
        verbose_name_plural = "Penalidades"

class VeiculoConfiscado(models.Model):
    tipo = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    dono = models.CharField(max_length=50)
    placa = models.CharField(max_length=20)
    data_de_confiscamento = models.DateField()
    tem_documento = models.CharField(max_length=400)

    def __str__(self):
        return self.tipo

    class Meta:
        verbose_name = "VeiculoConfiscado"
        verbose_name_plural = "VeiculosConfiscados"

class ResultadoInvestigacao(models.Model):
    descricao = models.CharField(max_length=500)
    denuncia = models.ForeignKey(Denuncia, on_delete=models.CASCADE)
    penalidade = models.ForeignKey(Penalidade, on_delete=models.CASCADE)


    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "ResultadoInvestigacao"
        verbose_name_plural = "ResultadosInvestigacao"

class Historico(models.Model):
    cidadão = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=100000)
    culpado = models.CharField(max_length=100000)


    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Historico"
        verbose_name_plural = "Historicos"

class Investigacao(models.Model):
    descricao = models.CharField(max_length=500)
    policial = models.ForeignKey(Policial, on_delete=models.CASCADE)


    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Investigacao"
        verbose_name_plural = "Investigacoes"

class RelatorioPorRua(models.Model):
    data = models.DateField()
    rua = models.ForeignKey(Rua, on_delete=models.CASCADE)
    investigacoes_concluidas = models.CharField(max_length=100)
    


    def __str__(self):
        return self.investigacoes_concluidas

    class Meta:
        verbose_name = "RelatorioPorRua"
        verbose_name_plural = "RelatoriosPorRua"

class RelatorioEstatistico(models.Model):
    data = models.DateField()
    infracao_mais_comum = models.CharField(max_length=300)
    


    def __str__(self):
        return self.infracao_mais_comum

    class Meta:
        verbose_name = "RelatorioEstatistico"
        verbose_name_plural = "RelatoriosEstatisticos"

class Login(models.Model):
    email = models.EmailField()
    senha = models.CharField(max_length=200)
    


    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Login"
        verbose_name_plural = "Logins"