from django.db import models
from .utils import encrypt_message, decrypt_message
from django.contrib.auth.models import User


class Categoria(models.Model):
    nombre = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.nombre

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField() 
    mensaje_cifrado = models.TextField(default='')  
    fecha = models.DateTimeField(auto_now_add=True) 

    def save(self, *args, **kwargs):
        self.mensaje_cifrado = encrypt_message(self.mensaje)
        super().save(*args, **kwargs)

    def get_mensaje(self):
        return decrypt_message(self.mensaje_cifrado)

    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='peliculas/')
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class Carrito(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    peliculas = models.ManyToManyField(Pelicula, through='CarritoItem')

class CarritoItem(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)