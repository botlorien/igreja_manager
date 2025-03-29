from django.contrib import admin
from .models import Membro

@admin.register(Membro)
class MembroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'phone', 'igreja')
    list_filter = ('igreja',)
    search_fields = ('nome', 'email')
