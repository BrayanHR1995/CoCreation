from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^account/$', Inicio.as_view(), name='inicio'),
    url(r'^account/inicio/$', Inicio.as_view(), name='inicio'),


    url(r'^account/areas/$', ListarArea.as_view(), name='listar_areas'),
    url(r'^account/areas/add/$', RegistroArea.as_view(), name='agregar_areas'),
    url(r'^account/areas/edit/(?P<pk>\d+)$', ModificarArea.as_view(), name='modificar_areas'),
    url(r'^account/areas/ver/(?P<pk>\d+)$', VerArea.as_view(), name='ver_areas'),
    url(r'^account/areas/del/(?P<pk>\d+)$', EliminarArea.as_view(), name='eliminar_areas'),


    url(r'^account/usuarios/$', ListarUsuarios.as_view(), name='usuarios'),
    url(r'^account/usuarios/add/$', RegistroUsuarios.as_view(), name='registar_usuarios'),
    url(r'^account/usuarios/edit/(?P<pk>\d+)$', ModificarUsuarios.as_view(), name='modificar_Usuarios'),
    url(r'^account/usuarios/ver/(?P<pk>\d+)$', VerUsuario.as_view(), name='ver_Usuarios'),
    url(r'^account/usuarios/del/(?P<pk>\d+)$', EliminarUsuarios.as_view(), name='eliminar_Usuarios'),


    url(r'^account/retos/$', ListarReto.as_view(), name='listar_retos'),
    url(r'^account/retos/add/$', RegistroReto.as_view(), name='agregar_retos'),
    url(r'^account/retos/edit/(?P<pk>\d+)$', ModificarReto.as_view(), name='modificar_retos'),
    url(r'^account/retos/del/(?P<pk>\d+)$', EliminarReto.as_view(), name='eliminar_retos'),
    url(r'^account/retos/ver/(?P<pk>\d+)$', VerReto.as_view(), name='ver_reto'),


    url(r'^account/estadisticas/$', estadisticas, name='estadisticas'),
    url(r'^account/emprendedor/productos$', productos, name='productos'),
    url(r'^account/emprendedor/equipo', equipo, name='equipo'),
    url(r'^account/emprendedor/misretos', misretos, name='misretos'),
    url(r'^account/emprendedor/dashboard', dashboard, name='misretos'),
    url(r'^account/emprendedor/actividad_reciente', actividad_reciente, name='actividad_reciente'),
    url(r'^account/emprendedor/mis_tareas', mis_tareas, name='mis_tareas'),

]

