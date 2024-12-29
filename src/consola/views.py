from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Consola, Juego, Jugador
from .forms import ConsolaForm, JuegoForm, JugadorForm

# Create your views here.
def index(request):
    return render(request, "consola/index.html")

def about(request):
    return render(request, "consola/about.html")

@login_required
def consola_list(request):
    query = Consola.objects.all()
    search_query = request.GET.get('q')
    if search_query:
        query = query.filter(nombre__icontains=search_query)
    context = {"consolas": query, "search_query": search_query}
    return render(request, "consola/consola_list.html", context)

@login_required
def consola_create(request):
    if request.method == "GET":
        form = ConsolaForm()
    if request.method == "POST":
        form = ConsolaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("consola:consola_list")
    return render(request, "consola/consola_form.html", {"form": form})

@login_required
def consola_edit(request, pk):
    consola = Consola.objects.get(pk=pk)
    if request.method == "POST":
        form = ConsolaForm(request.POST, instance=consola)
        if form.is_valid():
            form.save()
            return redirect("consola:consola_list")
    else:
        form = ConsolaForm(instance=consola)
    return render(request, "consola/consola_form.html", {"form": form, "consola": consola})

@login_required
def consola_delete(request, pk):
    consola = Consola.objects.get(pk=pk)
    if request.method == "POST":
        consola.delete()
        return redirect("consola:consola_list")
    return render(request, "consola/consola_confirm_delete.html", {"consola": consola})

@login_required
def juego_list(request):
    query = Juego.objects.all()
    search_query = request.GET.get('q')
    if search_query:
        query = query.filter(nombre_juego__icontains=search_query)
    context = {"juegos": query, "search_query": search_query}
    return render(request, "consola/juego_list.html", context)

@login_required
def juego_create(request):
    if request.method == "GET":
        form = JuegoForm()
    if request.method == "POST":
        form = JuegoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("consola:juego_list")
    return render(request, "consola/juego_form.html", {"form": form})

@login_required
def juego_edit(request, pk):
    juego = Juego.objects.get(pk=pk)
    if request.method == "POST":
        form = JuegoForm(request.POST, instance=juego)
        if form.is_valid():
            form.save()
            return redirect("consola:juego_list")
    else:
        form = JuegoForm(instance=juego)
    return render(request, "consola/juego_form.html", {"form": form, "juego": juego})

@login_required
def juego_delete(request, pk):
    juego = Juego.objects.get(pk=pk)
    if request.method == "POST":
        juego.delete()
        return redirect("consola:juego_list")
    return render(request, "consola/juego_confirm_delete.html", {"juego": juego})

@login_required
def jugador_list(request):
    query = Jugador.objects.all()
    search_query = request.GET.get('q')
    if search_query:
        query = query.filter(dni__icontains=search_query)
    context = {"jugadores": query, "search_query": search_query}
    return render(request, "consola/jugador_list.html", context)

@login_required
def jugador_create(request):
    if request.method == "GET":
        form = JugadorForm()
    if request.method == "POST":
        form = JugadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("consola:jugador_list")
    return render(request, "consola/jugador_form.html", {"form": form})

@login_required
def jugador_edit(request, pk):
    jugador = Jugador.objects.get(pk=pk)
    if request.method == "POST":
        form = JugadorForm(request.POST, instance=jugador)
        if form.is_valid():
            form.save()
            return redirect("consola:jugador_list")
    else:
        form = JugadorForm(instance=jugador)
    return render(request, "consola/jugador_form.html", {"form": form, "jugador": jugador})

@login_required
def jugador_delete(request, pk):
    jugador = Jugador.objects.get(pk=pk)
    if request.method == "POST":
        jugador.delete()
        return redirect("consola:jugador_list")
    return render(request, "consola/jugador_confirm_delete.html", {"jugador": jugador})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('consola:index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})