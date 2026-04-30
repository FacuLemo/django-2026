from django.contrib.auth.models import User
from django.db import models


class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)
    color = models.CharField(max_length=30)

    def __str__(self):
        return f"Etiqueta: {self.nombre}"


class Tarea(models.Model):
    nombre = models.CharField(max_length=100)
    completada = models.BooleanField(
        default=False,
        help_text="¿La tarea está completada?",
        verbose_name="Finalización de la tarea"
    )
    fecha_completado = models.DateField()
    fecha_creacion = models.DateTimeField(auto_now=True)
    responsable = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="responsable",
        default=None,
        blank=True,
        null=True,
    )
    etiqueta = models.ManyToManyField(
        Etiqueta,
        default=None,
        blank=True,
        related_name="etiquetas",
    )
    activo = models.BooleanField(default=True, help_text="Verdadero si NO está archivado")
    imagen = models.ImageField(upload_to="card_image/", null=True, blank=True)

    def nombre_mayuscula(self):
        return f"{self.nombre.upper()}"

    def __str__(self):
        return f"Soy la tarea: {self.nombre}"
    
    class Meta:
        verbose_name = "Tarea de proyecto"
        verbose_name_plural = "Tareas de los proyectos"
        ordering = ["-id"]



# si creo o modifico un modelo, debo correr:
# > python3 manage.py makemigrations
# > python3 manage.py migrate
