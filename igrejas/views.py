from django.shortcuts import render, get_object_or_404
from .models import Igreja
from django.contrib.auth.decorators import login_required

@login_required
def igreja_list_view(request):
    igrejas = Igreja.objects.all()
    return render(request, 'igrejas/igrejas_cards.html', {'igrejas': igrejas})

@login_required
def igreja_detail_view(request, igreja_id):
    igreja = get_object_or_404(Igreja, id=igreja_id)
    return render(request, 'igrejas/igreja_detail.html', {'igreja': igreja})
