from django.shortcuts import render, get_object_or_404
from .models import Cursos
# Create your views here.

def index(request):
    cursos=Cursos.objects.all()
    context={
        'cursos':cursos
    }
    return render(request, 'index.html', context)

def detalhe(request, id):
    detalhes=get_object_or_404(Cursos,id=id)
    context={
        'detalhes':detalhes
    }
    return render(request, 'curso.html', context)

def sobre_mim(request):
    return render(request, 'sobremim.html')
