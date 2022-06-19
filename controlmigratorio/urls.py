from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('perfil/<int:pasaporte_ciudadano>', views.perfilMigratorio, name='perfil'),
    path('buscar', views.bucarPerfil, name='buscar'),
    path('registrar-movimiento', views.registrarMovimiento, name='registrar'),
    path('activar-alerta/<int:pasaporte>', views.activarAlerta, name='activar'),
    path('desactivar-alerta/<int:pasaporte>', views.desactivarAlerta, name='desactivar'),

]
