
from datetime import datetime
from todolist.models import Etiqueta
from django.core.cache import cache
from django.utils.translation import gettext_lazy as _


def year_context(request):
    year = datetime.now().year
    return {"year":year}

def bienvenido_context(request):
    if request.user.is_authenticated:
        mensaje = _(f"Bienvenido {request.user.username}")
    else:
        mensaje = _("Bienvenido invitado!! Logeate!!")
    return {"mensaje_bienvenida":mensaje}

def etiquetas_context(request):
    etiquetas = cache.get("todolist_etiquetas")
    if etiquetas is None:
        etiquetas = list(Etiqueta.objects.all())
        cache.set('todolist_etiquetas', etiquetas, 3600) #1 hs segundos
        #print("nueva caché seteada.")

    return {"etiquetas_populares":etiquetas}


