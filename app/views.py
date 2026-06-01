from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import *


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return render(request, "login.html", {"erro": "Usuário ou senha inválidos"})

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("login")


def proteger(cls):
    cls.dispatch = method_decorator(login_required)(cls.dispatch)
    return cls


@proteger
class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


@proteger
class UsuarioView(View):
    def get(self, request):
        usuarios = Usuario.objects.all()
        return render(request, 'usuario.html', {'usuarios': usuarios})


@proteger
class PolicialView(View):
    def get(self, request):
        policiais = Policial.objects.all()
        return render(request, 'policial.html', {'policiais': policiais})


@proteger
class DenunciasView(View):
    def get(self, request):

        if request.user.is_staff:
            denuncias = Denuncia.objects.all()
        else:
            denuncias = Denuncia.objects.filter(
                denunciante__email=request.user.username
            )

        return render(request, 'denuncia.html', {'denuncias': denuncias})


@proteger
class RuasView(View):
    def get(self, request):
        ruas = Rua.objects.all()
        return render(request, 'rua.html', {'ruas': ruas})


@proteger
class PenalidadesView(View):
    def get(self, request):
        penalidades = Penalidade.objects.all()
        return render(request, 'penalidade.html', {'penalidades': penalidades})


@proteger
class VeiculosConfiscadosView(View):
    def get(self, request):
        veiculosconfiscados = VeiculoConfiscado.objects.all()
        return render(request, 'veiculosconfiscados.html', {'veiculosconfiscados': veiculosconfiscados})


@proteger
class EvidenciaView(View):
    def get(self, request):
        evidencias = Evidencia.objects.all()
        return render(request, 'evidencia.html', {'evidencias': evidencias})


@proteger
class TipoInfracaoView(View):
    def get(self, request):
        tipos_infracao = TipoInfracao.objects.all()
        return render(request, 'tipo_infracao.html', {'tipos_infracao': tipos_infracao})


@proteger
class ResultadoInvestigacaoView(View):
    def get(self, request):
        resultados_investigacao = ResultadoInvestigacao.objects.all()
        return render(request, 'resultado_investigacao.html', {
            'resultados_investigacao': resultados_investigacao
        })


@proteger
class HistoricoView(View):
    def get(self, request):
        historicos = Historico.objects.all()
        return render(request, 'historico.html', {'historicos': historicos})


@proteger
class InvestigacaoView(View):
    def get(self, request):
        investigacoes = Investigacao.objects.all()
        return render(request, 'investigacao.html', {'investigacoes': investigacoes})


@proteger
class RelatorioPorRuaView(View):
    def get(self, request):
        relatorios_por_rua = RelatorioPorRua.objects.all()
        return render(request, 'relatorio_por_rua.html', {
            'relatorios_por_rua': relatorios_por_rua
        })


@proteger
class RelatorioEstatisticoView(View):
    def get(self, request):
        relatorios_estatisticos = RelatorioEstatistico.objects.all()
        return render(request, 'relatorio_estatistico.html', {
            'relatorios_estatisticos': relatorios_estatisticos
        })