from django.contrib import admin

from .models import Etiqueta, Tarea

admin.site.register(Etiqueta)


@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "completada", "responsable")
    list_filter = ("completada",)
    search_fields = ("nombre",)
