from django.db import models

# Create your models here.
class Aluno(models.Model):
    Nome = models.CharField(max_length=100)
    RA = models.CharField(max_length=30)
    Curso = models.CharField(max_length=100)