from django.db import models

class Videojuego(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título")
    plataforma = models.CharField(max_length=50, verbose_name="Plataforma")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio (CLP)")
    stock = models.IntegerField(default=0, verbose_name="Stock disponible")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de registro")

    class Meta:
        verbose_name = "Videojuego"
        verbose_name_plural = "Videojuegos"
        ordering = ['titulo']

    def __str__(self):
        return f"{self.titulo} ({self.plataforma}) - ${self.precio}"