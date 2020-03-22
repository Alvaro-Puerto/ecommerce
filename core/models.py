from django.db import models
from django.urls import reverse
# Create your models here.
position_choices = (
    ("C","Centro"),
    ("D", "Derecha")
)
class Slider(models.Model):
    image = models.ImageField(upload_to="media")
    texto = models.TextField(max_length=500)
    texto_pequeño = models.TextField(max_length=500)
    posicion = models.CharField(max_length=1, choices=position_choices)


class Articulo(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    imagen_presentacion = models.ImageField(upload_to="media", null=True)
    descripcion = models.TextField(max_length=500)
    imagen_referencia = models.ManyToManyField("ImagenRefencia")
    precio = models.FloatField(default=0.00)
    descuento = models.FloatField(default=0.00)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        
        return reverse('core:producto', kwargs={'pk': self.pk})

   
class ImagenRefencia(models.Model):
    imagen = models.ImageField(upload_to="media")
    descripcion = models.TextField(max_length=50, null=True, blank=True)