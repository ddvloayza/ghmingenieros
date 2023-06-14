from django.urls import path

from apps.core.views import Error404View

from .views import AboutView, CapacitacionView, ElaboracionView, EscuelaView, HomeView, MetalografiaView, MisionView, PruebaView, ServicesView, ContactView, EnsayosView, TratamientoView, VerificacionView

app_name = "core"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("mision/", MisionView.as_view(), name="mision"),
    path("services/", ServicesView.as_view(), name="services"),
    path("ensayos_no_destructivos/", EnsayosView.as_view(), name="ensayos-no-destructivos"),
    path("capacitacion_y_certificacion_ndt_aws/", CapacitacionView.as_view(), name="capacitacion-y-certificacion-ndt-aws"),
    path("elaboracion_y_calificacion_procedimiento/", ElaboracionView.as_view(), name="elaboracion-y-calificacion-procedimiento"),
    path("escuela_soldadura/", EscuelaView.as_view(), name="escuela-soldadura"),
    path("metalografia/", MetalografiaView.as_view(), name="metalografia"),
    path("prueba_de_vacio_soldaduras/", PruebaView.as_view(), name="prueba-de-vacio-soldaduras"),
    path("tratamiento_termico_dureza/", TratamientoView.as_view(), name="tratamiento-termico-dureza"),
    path("verificacion_de_materiales/", VerificacionView.as_view(), name="verificacion-de-materiales"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("404/", Error404View.as_view(), name="error-404"),
]
