from django.shortcuts import render
from .models import Estudantes

# Create your views here.

def home(request):
    return render(request, 'home.html')

def estudantes(request):
    #Salvar para BD
    estudante = Estudantes()
    estudante.nome = request.POST.get('nome')
    estudante.curso = request.POST.get('curso')
    estudante.disciplina = request.POST.get('disciplina')
    estudante.ano = request.POST.get('ano')
    estudante.save()

    #Exibir dados
    estudantes  = {
        'estudantes': Estudantes.objects.all()
    }
    return render(request, 'estudantes.html', estudantes)

    
    
    