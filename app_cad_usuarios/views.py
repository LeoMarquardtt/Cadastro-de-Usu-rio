from django.shortcuts import render, redirect
from .models import Usuario


def home(request):
    usuarios = Usuario.objects.all()
    return render(request,'usuarios/home.html', {"usuarios" : usuarios})


def salvar(request):
    vnome = request.POST.get("nome")
    vidade = request.POST.get("idade")
    Usuario.objects.create(nome=vnome, idade=vidade)
    usuarios = Usuario.objects.all()
    return redirect('home')

def atualizar(request, id):
    usuario = Usuario.objects.get(id=id)
    return render(request, "usuarios/update.html", {"usuario" : usuario} )

def update(request, id):
    nome = request.POST.get("nome")
    idade = request.POST.get("idade")
    usuario = Usuario.objects.get(id = id)
    usuario.nome = nome
    usuario.idade = idade
    usuario.save()
    return redirect('home')

def delete(request, id):
    usuario = Usuario.objects.get(id = id)
    usuario.delete()
    return redirect('home')
