from django.db import models

# Create your models here.

class ListaDeTarefas(models.Model):
	tarefa 		= models.CharField(max_length=200)
	descricao   = models.TextField()
	data   		= models.DateField()


	def __str__(self):
		return self.tarefa