# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tipodocumento(models.Model):
    nombretipo = models.CharField(max_length=50)

class Rol(models.Model):
    nombrerol = models.CharField(max_length=50)

    def __str__(self):
        return self.nombrerol

class Estado(models.Model):
    nombreestado = models.CharField(max_length=50)

class Usuario(models.Model):
    nombres = models.CharField(max_length=500)
    edad = models.CharField(max_length=50)
    profesion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    celular = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password1 = models.CharField(max_length=50)
    #tipodocumento = models.ForeignKey(Tipodocumento, null=True, blank=True, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, null=True, blank=True, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, null=True, blank=True, on_delete=models.CASCADE)
    usuario = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)

