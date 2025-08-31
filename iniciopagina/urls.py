from django.urls import path
from .views import crear_nota, lista_notas, inicio, crear_alumno, lista_alumnos, crear_materia, lista_materias

urlpatterns = [
    path("", inicio, name="inicio"),
    path("notas/crear/", crear_nota, name="crear_nota"),
    path("notas/", lista_notas, name="lista_notas"),
    path("alumnos/crear/", crear_alumno, name="crear_alumno"),
    path("alumnos/", lista_alumnos, name="lista_alumnos"),
    path("materias/crear/", crear_materia, name="crear_materia"),
    path("materias/", lista_materias, name="lista_materias"),
]