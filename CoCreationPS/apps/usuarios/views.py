# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
# Create your views here.
from forms import *
from ..gestion.forms import *

class RegistroEmprendimiento(CreateView):
    model = Usuario
    template_name = "front/signup.html"
    form_class = RegistroForm
    second_form_class = EmprendimientoForm
    success_url = "/login/"

    def get_context_data(self, **kwargs):
        context = super(RegistroEmprendimiento, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            post = form.save(commit=False)
            post2 = form2.save(commit=False)
            #str(post.email).split("@")[0]
            u1 = User.objects.create_user(username=post.email, email=post.email, password=post.password1)
            u1.save()
            u = Usuario(usuario=u1, nombres=post.nombres, edad=post.edad, profesion=post.profesion, telefono=post.telefono, celular=post.celular, rol_id=1, estado_id=1)
            u.save()
            e = Emprendimiento(usuario=u1, nombre_emprendimiento=post2.nombre_emprendimiento, descripcion=post2.descripcion, numero_emprendedores=post2.numero_emprendedores,
            numero_colaboradores=post2.numero_colaboradores, portafolio=post2.portafolio, clientes=post2.clientes,
            vinculo_parquesoft = post2.vinculo_parquesoft, cual_vinculo=post2.cual_vinculo, medio=post2.medio, expectativas=post2.expectativas,
            recibir=post2.recibir, aporte=post2.aporte)
            e.save()

            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))

def registro(request):
    return render(request, "front/signup.html", {})

