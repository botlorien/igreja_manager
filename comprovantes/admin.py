from django.contrib import admin
from .models import Comprovante

@admin.register(Comprovante)
class ComprovanteAdmin(admin.ModelAdmin):
    list_display = ('membro', 'tipo', 'valor', 'data_comprovante')
    list_filter = ('tipo', 'data_comprovante')
    search_fields = ('membro__nome',)
    date_hierarchy = 'data_comprovante'
