from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
# mostra las tareas y quien las hizo 
    def __str__(self):
        return self.title + '- by' + self.user.username
    


class Project(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    apaterno = models.CharField(max_length=50, verbose_name= "Apellido paterno")
    amaterno = models.CharField(max_length=50, verbose_name= "Apellido materno")
    correo = models.EmailField(max_length=50, verbose_name= "Correo")
    hora = models.DateTimeField()
    comentario = models.TextField(max_length=200, verbose_name= "Comentario")

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=64)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='static/img', null=True, verbose_name="imagen")

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'
