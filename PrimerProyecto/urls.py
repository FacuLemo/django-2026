
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from usuarios.views import registrarse
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [ # Todo lo que tenga templates (front) se localiza (traduce)
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/register", registrarse, name="register"),
]

urlpatterns += i18n_patterns(
    path("admin/", admin.site.urls),
    path("", include("saludo.urls")),
    path("tareas/", include("todolist.urls")),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
