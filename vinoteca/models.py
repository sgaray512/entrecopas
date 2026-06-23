from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

class Bodega(models.Model):
    nombre = models.CharField(max_length=50)
    provincia = models.CharField(max_length=30)
    descripcion = models.TextField(max_length=100)
    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Vino(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=250)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to='vinos/')
    bodega = models.ForeignKey(
        Bodega,
        on_delete=models.CASCADE,
        related_name='vinos'
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='vinos'
    )
    def __str__(self):
        return self.nombre

class Resenia(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    vino = models.ForeignKey(
        Vino,
        on_delete=models.CASCADE
    )
    comentario = models.TextField(max_length=100)
    puntuacion = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])
    fecha = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.usuario} - {self.vino}"