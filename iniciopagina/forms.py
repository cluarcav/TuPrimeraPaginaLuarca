from django import forms
from .models import Alumno, Materia, Nota

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ["nombre", "email"]

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ["nombre"]

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ["alumno", "materia", "nota"] 
class BuscarAlumnoForm(forms.Form):
    q = forms.CharField(
        label="Buscar alumno",
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Nombre"})
    )