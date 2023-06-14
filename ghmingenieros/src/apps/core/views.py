from django.views import View
from django.http import JsonResponse
from django.views.generic import TemplateView, ListView
from django.core.paginator import Paginator
from django.views.generic.detail import DetailView


from apps.customuser.models.customuser import CustomWebPage, Banner
from django.db.models import Prefetch


class HomeView(TemplateView):
    template_name = "core/index.html"


class AboutView(TemplateView):
    template_name = "core/about.html"


class MisionView(TemplateView):
    template_name = "core/mision.html"


class ServicesView(TemplateView):
    template_name = "core/services.html"


class EnsayosView(TemplateView):
    template_name = "core/services/ensayos-no-destructivas.html"


class CapacitacionView(TemplateView):
    template_name = "core/services/capacitacion-y-certificacion-ndt-aws.html"

class ElaboracionView(TemplateView):
    template_name = "core/services/elaboracion-y-calificacion-procedimiento.html"

class EscuelaView(TemplateView):
    template_name = "core/services/escuela-soldadura.html"

class MetalografiaView(TemplateView):
    template_name = "core/services/metalografia.html"

class PruebaView(TemplateView):
    template_name = "core/services/prueba-de-vacio-soldaduras.html"

class TratamientoView(TemplateView):
    template_name = "core/services/tratamiento-termico-dureza.html"


class VerificacionView(TemplateView):
    template_name = "core/services/verificacion-de-materiales.html"


class ContactView(TemplateView):
    template_name = "core/contact.html"


class Error404View(TemplateView):
    template_name = "core/errors/404.html"
