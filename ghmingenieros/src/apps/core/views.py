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


class ContactView(TemplateView):
    template_name = "core/contact.html"


class Error404View(TemplateView):
    template_name = "core/errors/404.html"
