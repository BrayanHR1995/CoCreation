from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from views import *
urlpatterns = [
    url(r'^account/$', dashboard.as_view(), name='inicio'),
    url(r'^account/inicio/$', dashboard.as_view(), name='inicio'),


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

    url(r'^account/emprendedor/productos$', productos.as_view(), name='productos'),
    url(r'^account/emprendedor/productos/add$', RegistroProductos.as_view(), name='agregar_productos'),
    url(r'^account/emprendedor/productos/del/(?P<pk>\d+)$', EliminarProductos.as_view(), name='eliminar_productos'),
    url(r'^account/emprendedor/productos/edit/(?P<pk>\d+)$', ModificarProductos.as_view(), name='modificar_productos'),
    url(r'^account/emprendedor/productos/ver/(?P<pk>\d+)$', VerProductos.as_view(), name='ver_productos'),

    url(r'^account/emprendedor/equipo', equipo.as_view(), name='equipo'),
    url(r'^account/emprendedor/misretos', misretos, name='misretos'),
    url(r'^account/emprendedor/dashboard', dashboard.as_view(), name='dashboard'),
    url(r'^account/emprendedor/actividad_reciente', actividad_reciente, name='actividad_reciente'),



    url(r'^account/emprendedor/mis_tareas', mis_tareas.as_view(), name='mis_tareas'),
    url(r'^account/emprendedor/tareas/add$', RegistroTareas.as_view(), name='agregar_tareas'),
    url(r'^account/emprendedor/tareas/del/(?P<pk>\d+)$', EliminarTareas.as_view(), name='eliminar_tareas'),
    url(r'^account/emprendedor/tareas/edit/(?P<pk>\d+)$', ModificarTareas.as_view(), name='modificar_tareas'),
    url(r'^account/emprendedor/tareas/ver/(?P<pk>\d+)$', VerTareas.as_view(), name='ver_tareas'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

