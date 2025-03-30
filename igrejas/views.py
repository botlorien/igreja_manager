from django.shortcuts import render, get_object_or_404
from .models import Igreja
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView


@login_required
def igreja_list_view(request):
    igrejas = Igreja.objects.all()
    return render(request, 'igrejas/igrejas_cards.html', {'igrejas': igrejas})

@login_required
def igreja_detail_view(request, igreja_id):
    igreja = get_object_or_404(Igreja, id=igreja_id)
    return render(request, 'igrejas/igreja_detail.html', {'igreja': igreja})


class IgrejaCreateView(CreateView):
    model = Igreja
    fields = ['nome', 'cidade', 'estado', 'endereco', 'contato', 'imagem_da_igreja']
    template_name = 'igrejas/form.html'
    success_url = '/'