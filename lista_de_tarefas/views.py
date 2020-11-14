from django.shortcuts import render
from .models import ListaDeTarefas
# Create your views here.


def mostrar_tarefas(request):
	lista_de_tarefas = ListaDeTarefas.objects.all()
	return render(request,"index.html",{'lista_de_tarefas':lista_de_tarefas})