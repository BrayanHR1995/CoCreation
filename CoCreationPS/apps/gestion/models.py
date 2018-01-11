# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..usuarios.models import *
# Create your models here.


class Emprendimiento(models.Model):
    nombre_emprendimiento = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    numero_emprendedores = models.CharField(max_length=10)
    numero_colaboradores = models.CharField(max_length=10)
    portafolio = models.CharField(max_length=300)
    clientes = models.CharField(max_length=300)
    vinculo_parquesoft = models.CharField(max_length=10)
    cual_vinculo = models.CharField(max_length=100)
    medio = models.CharField(max_length=100)
    expectativas = models.CharField(max_length=100)
    recibir = models.CharField(max_length=100)
    aporte = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    emprendimiento = models.ForeignKey(Emprendimiento, null=True, blank=True, on_delete=models.CASCADE)

class PortafolioPS(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    ruta_imagen = models.CharField(max_length=100)
    emprendimiento = models.ForeignKey(Emprendimiento, null=True, blank=True, on_delete=models.CASCADE)

class Area(models.Model):
    nombre_area = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    ruta_imagen = models.ImageField( upload_to = 'imagenes/areas/')
    usuario_responsable = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)

class Fase(models.Model):
    nombre_fase = models.CharField(max_length=100)


class Reto(models.Model):
    nombre_reto = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    tiempo = models.CharField(max_length=50)
    ruta_imagen = models.CharField(max_length=100)
    area = models.ForeignKey(Area, null=True, blank=True, on_delete=models.CASCADE)
    fase  = models.ForeignKey(Fase, null=True, blank=True, on_delete=models.CASCADE)

class Tarea(models.Model):
    nombre_tarea = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    fechainicio = models.CharField(max_length=50)
    fechafin = models.CharField(max_length=50)
    usuario = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, null=True, blank=True, on_delete=models.CASCADE)
    reto = models.ForeignKey(Reto, null=True, blank=True, on_delete=models.CASCADE)