from django.urls import path

from apps.core.views import Error404View

from .views import AboutView, HomeView, MisionView, ServicesView, ContactView

app_name = "core"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("mision/", MisionView.as_view(), name="mision"),
    path("services/", ServicesView.as_view(), name="services"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("404/", Error404View.as_view(), name="error-404"),
]
