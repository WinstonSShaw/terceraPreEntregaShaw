from django.db import models

# Create your models here.
class Consola(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nombre

class Juego(models.Model):
    consola = models.ForeignKey(Consola, on_delete=models.SET_NULL, null=True)
    nombre_juego = models.CharField(max_length=255)
    fecha_inicio = models.DateField(null=True)

    def __str__(self):
        return f"{self.consola} - {self.nombre_juego}"

class Jugador(models.Model):
    juego = models.ForeignKey(Juego, on_delete=models.SET_NULL, null=True)
    dni = models.IntegerField()