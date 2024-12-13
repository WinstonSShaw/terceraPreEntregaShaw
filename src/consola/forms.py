from django import forms

from .models import Consola, Juego, Jugador

class ConsolaForm(forms.ModelForm):
    class Meta:
        model = Consola
        fields = "__all__"

class JuegoForm(forms.ModelForm):
    class Meta:
        model = Juego
        fields = "__all__"
        widgets = {
            "fecha_inicio": forms.DateInput(attrs={"type": "date"}),
        }

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = "__all__"