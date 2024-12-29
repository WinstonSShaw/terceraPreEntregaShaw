
from django.urls import path

from .views import about, index, consola_list, juego_list, jugador_list, consola_create, juego_create, jugador_create, consola_edit, consola_delete, juego_edit, juego_delete, jugador_edit, jugador_delete, register

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
    path("consola/<int:pk>/edit/", consola_edit, name="consola_edit"),
    path("consola/<int:pk>/delete/", consola_delete, name="consola_delete"),
    path("juego/<int:pk>/edit/", juego_edit, name="juego_edit"),
    path("juego/<int:pk>/delete/", juego_delete, name="juego_delete"),
    path("jugador/<int:pk>/edit/", jugador_edit, name="jugador_edit"),
    path("jugador/<int:pk>/delete/", jugador_delete, name="jugador_delete"),
    path('accounts/register/', register, name='register'),
]

