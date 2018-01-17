# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *

# Register your models here.

admin.site.register(Emprendimiento)
admin.site.register(Area)
admin.site.register(Reto)
admin.site.register(Tarea)

class AlbumImageInline(admin.TabularInline):
    model = Area
    extra = 3

class AlbumAdmin(admin.ModelAdmin):
    inlines = [ AlbumImageInline, ]

@admin.register(PortafolioPS)
class PortafolioAdmin(admin.ModelAdmin):
    pass