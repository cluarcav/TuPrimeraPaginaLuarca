from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=80)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} <{self.email}>"

class Materia(models.Model):
    nombre = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.nombre

class Nota(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, related_name="notas")
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name="notas")
    nota = models.DecimalField(max_digits=4, decimal_places=1)  

    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('alumno', 'materia')

    def __str__(self):
        return f"{self.alumno.nombre} – {self.materia.nombre}: {self.puntaje}"