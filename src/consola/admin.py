from django.contrib import admin

from .models import Consola, Juego, Jugador

# Register your models here.

@admin.register(Consola)
class ConsolaAdmin(admin.ModelAdmin):
    list_display = ("nombre",)

@admin.register(Juego)
class JuegoAdmin(admin.ModelAdmin):
    list_display = ("consola__nombre", "nombre_juego", "fecha_inicio",)

@admin.register(Jugador)
class JugadorAdmin(admin.ModelAdmin):
    list_display = ("juego", "dni",)

