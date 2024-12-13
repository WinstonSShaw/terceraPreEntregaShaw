from django.shortcuts import render, redirect

from .models import Consola, Juego, Jugador
from .forms import ConsolaForm, JuegoForm, JugadorForm

# Create your views here.
def index(request):
    return render(request, "consola/index.html")

def about(request):
    return render(request, "consola/about.html")

def consola_list(request):
    query = Consola.objects.all()
    context = {"consolas": query}
    return render(request, "consola/consola_list.html", context)

def consola_create(request):
    if request.method == "GET":
        form = ConsolaForm()
    if request.method == "POST":
        form = ConsolaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("consola:consola_list")
    return render(request, "consola/consola_form.html", {"form": form})

def juego_list(request):
    query = Juego.objects.all()
    context = {"juegos": query}
    return render(request, "consola/juego_list.html", context)

def juego_create(request):
    if request.method == "GET":
        form = JuegoForm()
    if request.method == "POST":
        form = JuegoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("consola:juego_list")
    return render(request, "consola/juego_form.html", {"form": form})

def jugador_list(request):
    query = Jugador.objects.all()
    context = {"jugadores": query}
    return render(request, "consola/jugador_list.html", context)

def jugador_create(request):
    if request.method == "GET":
        form = JugadorForm()
    if request.method == "POST":
        form = JugadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("consola:jugador_list")
    return render(request, "consola/jugador_form.html", {"form": form})