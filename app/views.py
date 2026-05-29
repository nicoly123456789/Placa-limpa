from django.shortcuts import render,redirect,get_object_or_404
from .models import *
# from .forms import LivroForms
from django.views import View
from django.contrib import messages

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

class UsuariosView(View):
    def get(self, request):
        usuarios = Usuario.objects.all()
        return render(request, 'usuario.html', {'usuarios': usuarios})

class DenunciasView(View):
    def get(self, request):
        denuncias = Denuncia.objects.all()
        return render(request, 'denuncia.html', {'denuncias': denuncias})

class RuasView(View):
    def get(self, request):
        ruas = Rua.objects.all()
        return render(request, 'rua.html', {'ruas': ruas})

class PenalidadesView(View):
    def get(self, request):
        penalidades = Penalidade.objects.all()
        return render(request, 'penalidade.html', {'penalidades': penalidades})

class VeiculosConfiscadosView(View):
    def get(self, request):
        veiculosconfiscados = VeiculoConfiscado.objects.all()
        return render(request, 'veiculosconfiscados.html', {'veiculosconfiscados': veiculosconfiscados})

class EvidenciaView(View):
    def get(self, request):
        evidencias = Evidencia.objects.all()
        return render(request, 'evidencia.html', {'evidencias': evidencias})