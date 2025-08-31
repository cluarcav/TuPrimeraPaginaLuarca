from django.shortcuts import render, redirect
from django.db.models import Q
from .forms import AlumnoForm, MateriaForm, NotaForm, BuscarAlumnoForm
from .models import Alumno, Materia, Nota

def inicio(request):
    # Renderiza una página simple de inicio
    return render(request, "iniciopagina/inicio.html")

def crear_alumno(request):
    form = AlumnoForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("lista_alumnos")
    return render(request, "iniciopagina/alumno_form.html", {"form": form})

def lista_alumnos(request):
    form_buscar = BuscarAlumnoForm(request.GET or None)
    alumnos = Alumno.objects.all().order_by("nombre")
    if form_buscar.is_valid() and form_buscar.cleaned_data.get("q"):
        q = form_buscar.cleaned_data["q"]
        alumnos = alumnos.filter(Q(nombre__icontains=q) | Q(email__icontains=q))
    return render(
        request,
        "iniciopagina/alumno_list.html",
        {"alumnos": alumnos, "form_buscar": form_buscar},
    )

def crear_materia(request):
    form = MateriaForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("lista_materias")
    return render(request, "iniciopagina/materia_form.html", {"form": form})

def lista_materias(request):
    materias = Materia.objects.all().order_by("nombre")
    return render(request, "iniciopagina/materia_list.html", {"materias": materias})

def crear_nota(request):
    form = NotaForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("lista_notas")
    return render(request, "iniciopagina/nota_form.html", {"form": form})

def lista_notas(request):
    nota = Nota.objects.select_related("alumno", "materia").all().order_by(
        "alumno__nombre", "materia__nombre"
    )
    return render(request, "iniciopagina/nota_list.html", {"nota": nota})