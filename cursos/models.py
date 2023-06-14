from django.db import models

# Create your models here.
class Cursos(models.Model):
    nome_cursos = models.CharField(max_length=255)
    nome_coordenador = models.CharField(max_length=255)
    descricao = models.TextField()
    periodos = models.IntegerField()
    imagem = models.ImageField(upload_to='imagens')
    