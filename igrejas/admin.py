from django.contrib import admin
from .models import Igreja

@admin.register(Igreja)
class IgrejaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade', 'estado', 'contato')
    search_fields = ('nome', 'cidade', 'estado')
