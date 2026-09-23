from django.contrib import admin
from .models import Videojuego

@admin.register(Videojuego)
class VideojuegoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'plataforma', 'precio', 'stock', 'fecha_creacion')
    list_filter = ('plataforma',)
    search_fields = ('titulo', 'plataforma')
    ordering = ('titulo',)
    list_per_page = 20
    readonly_fields = ('fecha_creacion',)
