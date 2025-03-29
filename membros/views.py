from django.shortcuts import render, get_object_or_404
from .models import Membro
from igrejas.models import Igreja
from django.contrib.auth.decorators import login_required

@login_required
def lista_membros(request, igreja_id):
    igreja = get_object_or_404(Igreja, id=igreja_id)
    membros = Membro.objects.filter(igreja=igreja)
    return render(request, 'membros/membros_list.html', {
        'igreja': igreja,
        'membros': membros
    })
