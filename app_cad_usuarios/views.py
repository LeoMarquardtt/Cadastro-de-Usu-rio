from django.shortcuts import render
from .models import Usuario
def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    #Salvar os dados do site para o bd
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    #Exibir
    usuarios = {
        'usuarios' : Usuario.objects.all()
    }
    #Retorno dos dados
    return render(request,'usuarios/usuarios.html',usuarios)
