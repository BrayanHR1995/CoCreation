# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from forms import *
from ..usuarios.forms import *
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.models import User

# Create your views here.

# ACA EMPIEZA EL CRUD DE AREAS #
class EliminarArea(LoginRequiredMixin, DeleteView):
    model = Area
    template_name = "administrador/del_areas.html"
    success_url = ".."

class ListarArea(LoginRequiredMixin, ListView):
    model = Area
    template_name = "administrador/areas.html"


class VerArea(LoginRequiredMixin, UpdateView):
    model = Area
    fields = ['nombre_area', 'descripcion', 'ruta_imagen']
    template_name = "administrador/ver_areas.html"


class RegistroArea(LoginRequiredMixin, CreateView):
    model = Area
    template_name = "administrador/area_form.html"
    form_class = AreaForm
    success_url = ".."

    def get_context_data(self, **kwargs):
        context = super(RegistroArea, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'responsables_list' not in context:
            context['responsables_list'] = Usuario.objects.order_by('usuario_id')
        return context


    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            #u1 = User.objects.create_user(username=post.email, email=post.email, password=post.password1)
            #u1.save()
            print "USUARIO RESPONSABLE -> "+str(post.usuario_responsable)

            u = Area(usuario_responsable_id=1, nombre_area=post.nombre_area, descripcion=post.descripcion, ruta_imagen=post.ruta_imagen)
            u.save()

            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

class ModificarArea(LoginRequiredMixin, UpdateView):
    model = Area
    #form_class = AreaForm
    template_name = "administrador/area_edit.html"
    fields = ['nombre_area', 'descripcion', 'ruta_imagen']
    success_url = ".."



# ACA TERMINA EL CRUD DE AREAS #


# ACA EMPIEZA EL CRUD DE RETOS #

class EliminarReto(LoginRequiredMixin, DeleteView):
    model = Reto
    template_name = "administrador/del_retos.html"
    success_url = ".."

class ModificarReto(LoginRequiredMixin, UpdateView):
    model = Reto
    form_class = RetoForm
    template_name = "administrador/edit_retos.html"
    success_url = ".."


class ListarReto(LoginRequiredMixin, ListView):
    model = Reto
    template_name = "administrador/retos.html"
    paginate_by = 3

class VerReto(LoginRequiredMixin, ListView):
    model = Reto
    template_name = "administrador/ver_retos.html"


class RegistroReto(LoginRequiredMixin, CreateView):
    model = Reto
    template_name = "administrador/add_retos.html"
    form_class = RetoForm
    success_url = ".."

    def get_context_data(self, **kwargs):
        context = super(RegistroReto, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #u1 = User.objects.create_user(username=post.email, email=post.email, password=post.password1)
            #u1.save()
            u = Reto(area_id = 1, nombre_reto=post.nombre_reto, descripcion=post.descripcion, tiempo=post.tiempo, ruta_imagen=post.ruta_imagen)
            u.save()

            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))




# ACA EMPIEZA CRUD DE USUARIOS #

class RegistroUsuarios(LoginRequiredMixin, CreateView):
    model = Usuario
    template_name = "administrador/add_usuarios.html"
    form_class = RegistroForm
    success_url = ".."

    def get_context_data(self, **kwargs):
        context = super(RegistroUsuarios, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #u1 = User.objects.create_user(username=post.email, email=post.email, password=post.password1)
            #u1.save()
            u1 = User.objects.create_user(username=post.email, email=post.email, password=post.password1)
            u1.save()
            u = Usuario(usuario=u1, nombres=post.nombres, edad=post.edad, profesion=post.profesion,
                        telefono=post.telefono, celular=post.celular, rol_id=1, estado_id=1)
            u.save()

            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

class EliminarUsuarios(LoginRequiredMixin, DeleteView):
    model = User
    template_name = "administrador/del_usuarios.html"
    success_url = ".."


class ModificarUsuarios(LoginRequiredMixin, UpdateView):
    model = Usuario
    form_class = RegistroForm
    template_name = "administrador/edit_usuarios.html"
    success_url = ".."


class Inicio(LoginRequiredMixin, ListView):
    context_object_name = 'retos_list'
    template_name = "administrador/inicio.html"

    def get_queryset(self):
        return Reto.objects.order_by("-id")

    def get_context_data(self, **kwargs):
        context = super(Inicio, self).get_context_data(**kwargs)
        context['usuarios_list'] = Usuario.objects.order_by('-usuario__last_login')
        return context


class ListarUsuarios(LoginRequiredMixin, ListView):
    model = Usuario
    #queryset = Usuario.objects.filter(title__icontains='war')[:5]  # Get 5 books containing the title war
    template_name = "administrador/usuarios.html"
    paginate_by = 3

    def get_queryset(self):
        y = Usuario.objects.all().order_by('usuario')
        return y


class VerUsuario(ListView):
    model = Usuario
    template_name = "administrador/ver_usuarios.html"


@login_required
def inicio(request):
    print " User Staff--------" + str(request.user.is_staff)
    if request.user.is_staff == True:
        return render(request, "/admin/", {})
    else:
        return render(request, "emprendedor/dashboard.html", {})


def retos(request):
    return render(request, "administrador/retos.html", {})
def estadisticas(request):
    return render(request, "emprendedor/add_productos.html", {})

def index(request):
     return HttpResponseRedirect('/account/inicio')


#Emprendedor
class dashboard(LoginRequiredMixin,ListView):
    context_object_name = 'productos_list'
    template_name = "emprendedor/dashboard.html"
    model=User

    def get_queryset(self):
        id_eprendimiento = Emprendimiento.objects.filter(usuario_id=self.request.user.id)
        return PortafolioPS.objects.filter(emprendimiento_id=id_eprendimiento)

    def get_context_data(self, **kwargs):
        id_eprendimiento1 = Emprendimiento.objects.filter(usuario_id=self.request.user.id)
        context = super(dashboard, self).get_context_data(**kwargs)

        context['equipo_list'] = Equipo.objects.filter(emprendimiento_id=id_eprendimiento1)
        context['tarea_list'] = Tarea.objects.filter(usuario_id=self.request.user.id)
        return context




class equipo(LoginRequiredMixin, ListView):
    model = Equipo
    template_name = "emprendedor/equipo.html"

    def get_queryset(self):
        id_eprendimiento = Emprendimiento.objects.filter(usuario_id=self.request.user.id)
        return Equipo.objects.filter(emprendimiento_id=id_eprendimiento)


###Productos

class productos(LoginRequiredMixin, ListView):
    model = PortafolioPS
    template_name = "emprendedor/productos.html"

    def get_queryset(self):
        id_eprendimiento= Emprendimiento.objects.filter(usuario_id=self.request.user.id)
        return PortafolioPS.objects.filter(emprendimiento_id=id_eprendimiento)

class EliminarProductos(LoginRequiredMixin, DeleteView):
    model = PortafolioPS
    template_name = "emprendedor/del_productos.html"
    success_url = "/account/emprendedor/productos"

class ModificarProductos(LoginRequiredMixin, UpdateView):
    model = PortafolioPS
    form_class = ProductoForm
    template_name = "emprendedor/edit_productos.html"
    success_url = "/account/emprendedor/productos"

class VerProductos(LoginRequiredMixin, ListView):
    model = PortafolioPS
    form_class = ProductoForm
    template_name = "emprendedor/ver_productos.html"

class RegistroProductos(LoginRequiredMixin, CreateView):
    model = PortafolioPS
    template_name = "emprendedor/add_productos.html"
    form_class = ProductoForm
    success_url = "/account/emprendedor/productos"

    def get_context_data(self, **kwargs):
        context = super(RegistroProductos, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context


    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():

            post = form.save(commit=False)
            u = PortafolioPS(emprendimiento_id=3, nombre="ddd", descripcion="234",  ruta_imagen=post.ruta_imagen)
            u.save()

            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


##Tareas
class mis_tareas(LoginRequiredMixin, ListView):
    model = Tarea
    template_name = "emprendedor/mis_tareas.html"
    def get_queryset(self):
        return Tarea.objects.filter(usuario_id=self.request.user.id)

class EliminarTareas(LoginRequiredMixin, DeleteView):
    model = Tarea
    template_name = "emprendedor/del_tareas.html"
    success_url = "/account/emprendedor/mis_tareas"

class ModificarTareas(LoginRequiredMixin, UpdateView):
    model = Tarea
    form_class = TareaForm
    template_name = "emprendedor/edit_tareas.html"
    success_url = "/account/emprendedor/mis_tareas"

class VerTareas(LoginRequiredMixin, ListView):
    model = Tarea
    form_class = TareaForm
    template_name = "emprendedor/ver_tareas.html"

class RegistroTareas(LoginRequiredMixin, CreateView):
    model = Tarea
    template_name = "emprendedor/add_tareas.html"
    form_class = TareaForm
    success_url = "/account/emprendedor/mis_tareas"

    def get_context_data(self, **kwargs):
        context = super(RegistroTareas, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context


    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():

            post = form.save(commit=False)
            u = Tarea(reto_id=1, usuario_id=12, estado_id=1, nombre_tarea=post.nombre_tarea, descripcion=post.descripcion, fechainicio=post.fechainicio, fechafin=post.fechafin)
            u.save()

            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

def misretos(request):
    return render(request, "emprendedor/misretos.html", {})

def actividad_reciente( request):
    return render(request, "emprendedor/actividad_reciente.html", {})
