from django.shortcuts import render, get_object_or_404
from .models import Membro
from igrejas.models import Igreja
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView


@login_required
def lista_membros(request, igreja_id):
    igreja = get_object_or_404(Igreja, id=igreja_id)
    membros = Membro.objects.filter(igreja=igreja)
    return render(request, 'membros/membros_list.html', {
        'igreja': igreja,
        'membros': membros
    })

class MembroCreateView(CreateView):
    model = Membro
    fields = ['nome', 'email', 'phone', 'igreja']
    template_name = 'membros/form.html'
    success_url = '/'