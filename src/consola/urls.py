
from django.urls import path

from .views import about, index, consola_list, juego_list, jugador_list, consola_create, juego_create, jugador_create

app_name = "consola"

urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("consola/list/", consola_list, name="consola_list"),
    path("consola/create/", consola_create, name="consola_create"),
    path("juego/list", juego_list, name="juego_list"),
    path("juego/create/", juego_create, name="juego_create"),
    path("jugador/list/", jugador_list, name="jugador_list"),
    path("jugador/create/", jugador_create, name="jugador_create"),
]

