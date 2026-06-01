from django.contrib import admin
from app.views import login_view, logout_view
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', IndexView.as_view(), name='index'),
    path('rua/', RuasView.as_view(), name='ruas'),
    path('policial/', PolicialView.as_view(), name='policiais'),
    path('evidencia/', EvidenciaView.as_view(), name='evidencias'),
    path('tipo_infracao/', TipoInfracaoView.as_view(), name='tipos_infracao'),
    path('usuario/', UsuarioView.as_view(), name='usuarios'),
    path('denuncia/', DenunciasView.as_view(), name='denuncias'),
    path('penalidade/', PenalidadesView.as_view(), name='penalidades'),
    path('veiculosconfiscados/', VeiculosConfiscadosView.as_view(), name='veiculos_confiscados'),
    path('resultado_investigacao/', ResultadoInvestigacaoView.as_view(), name='resultados_investigacao'),
    path('historico/', HistoricoView.as_view(), name='historicos'),
    path('investigacao/', InvestigacaoView.as_view(), name='investigacoes'),
    path('relatorio_por_rua/', RelatorioPorRuaView.as_view(), name='relatorios_por_rua'),
    path('relatorio_estatistico/', RelatorioEstatisticoView.as_view(), name='relatorios_estatisticos'),
]