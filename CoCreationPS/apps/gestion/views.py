# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from forms import *
from ..usuarios.forms import *
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

# ACA EMPIEZA EL CRUD DE AREAS #
class EliminarArea(DeleteView):
    model = Area
    template_name = "administrador/del_areas.html"
    success_url = ".."

class ListarArea(ListView):
    model = Area
    template_name = "administrador/areas.html"


class VerArea(UpdateView):
    model = Area
    fields = ['nombre_area', 'descripcion', 'ruta_imagen']
    template_name = "administrador/ver_areas.html"


class RegistroArea(CreateView):
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

class ModificarArea(UpdateView):
    model = Area
    #form_class = AreaForm
    template_name = "administrador/area_edit.html"
    fields = ['nombre_area', 'descripcion', 'ruta_imagen']
    success_url = ".."



# ACA TERMINA EL CRUD DE AREAS #


# ACA EMPIEZA EL CRUD DE RETOS #

class EliminarReto(DeleteView):
    model = Reto
    template_name = "administrador/del_retos.html"
    success_url = ".."

class ModificarReto(UpdateView):
    model = Reto
    form_class = RetoForm
    template_name = "administrador/edit_retos.html"
    success_url = ".."


class ListarReto(ListView):
    model = Reto
    template_name = "administrador/retos.html"
    paginate_by = 3

class VerReto(ListView):
    model = Reto
    template_name = "administrador/ver_retos.html"


class RegistroReto(CreateView):
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

class RegistroUsuarios(CreateView):
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

class EliminarUsuarios(DeleteView):
    model = User
    template_name = "administrador/del_usuarios.html"
    success_url = ".."


class ModificarUsuarios(UpdateView):
    model = Usuario
    form_class = RegistroForm
    template_name = "administrador/edit_usuarios.html"
    success_url = ".."


class Inicio(ListView):
    context_object_name = 'retos_list'
    template_name = "administrador/inicio.html"

    def get_queryset(self):
        return Reto.objects.order_by("-id")

    def get_context_data(self, **kwargs):
        context = super(Inicio, self).get_context_data(**kwargs)
        context['usuarios_list'] = Usuario.objects.order_by('-usuario__last_login')
        return context


class ListarUsuarios(ListView):
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
        return render(request, "administrador/inicio.html", {})


def retos(request):
    return render(request, "administrador/retos.html", {})
def estadisticas(request):
    return render(request, "administrador/estadisticas.html", {})

def index(request):
     return HttpResponseRedirect('/account/inicio')


#Emprendedor
def productos(request):
    return render(request, "emprendedor/productos.html", {})
def equipo(request):
    return render(request, "emprendedor/equipo.html", {})
def misretos(request):
    return render(request, "emprendedor/misretos.html", {})
def dashboard(request):
    return render(request, "emprendedor/dashboard.html", {})
def actividad_reciente(request):
    return render(request, "emprendedor/actividad_reciente.html", {})
def mis_tareas(request):
    return render(request, "emprendedor/mis_tareas.html", {})