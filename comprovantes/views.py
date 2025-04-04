from django.shortcuts import render, redirect, get_object_or_404
from .models import Comprovante
from membros.models import Membro
from igrejas.models import Igreja
from .forms import ComprovanteForm
from .filters import ComprovanteFilter
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import openpyxl

@login_required
def lista_comprovantes(request, igreja_id):
    igreja = get_object_or_404(Igreja, id=igreja_id)
    membros = Membro.objects.filter(igreja=igreja)
    comprovantes = Comprovante.objects.filter(membro__in=membros).order_by('-data_comprovante')
    filtro = ComprovanteFilter(request.GET, queryset=comprovantes)

    return render(request, 'comprovantes/lista.html', {
        'igreja': igreja,
        'filtro': filtro,
        'comprovantes': filtro.qs
    })

@login_required
def adicionar_comprovante(request, igreja_id):
    igreja = get_object_or_404(Igreja, id=igreja_id)

    if request.method == 'POST':
        form = ComprovanteForm(request.POST, request.FILES, igreja=igreja)
        if form.is_valid():
            form.save()
            return redirect('comprovantes:lista', igreja_id=igreja.id)
    else:
        form = ComprovanteForm(igreja=igreja)

    return render(request, 'comprovantes/form.html', {
        'form': form,
        'igreja': igreja
    })

@login_required
def visualizar_comprovante(request, pk):
    comprovante = get_object_or_404(Comprovante, pk=pk)
    return render(request, 'comprovantes/visualizar.html', {'comprovante': comprovante})


@login_required
def editar_comprovante(request, pk):
    comprovante = get_object_or_404(Comprovante, pk=pk)
    igreja = comprovante.membro.igreja  # igreja do membro

    if request.method == 'POST':
        form = ComprovanteForm(request.POST, request.FILES, instance=comprovante, igreja=igreja)
        if form.is_valid():
            form.save()
            return redirect('comprovantes:lista', igreja_id=igreja.id)
    else:
        form = ComprovanteForm(instance=comprovante, igreja=igreja)

    return render(request, 'comprovantes/form.html', {
        'form': form,
        'comprovante': comprovante,
        'igreja': igreja
    })


@login_required
def exportar_excel(request, igreja_id):
    igreja = get_object_or_404(Igreja, id=igreja_id)
    membros = Membro.objects.filter(igreja=igreja)
    comprovantes = Comprovante.objects.filter(membro__in=membros)

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = 'Comprovantes'

    ws.append(['Membro', 'Tipo', 'Valor', 'Data', 'Arquivo'])

    for c in comprovantes:
        ws.append([
            c.membro.nome,
            c.get_tipo_display(),
            str(c.valor),
            c.data_comprovante.strftime('%d/%m/%Y'),
            c.arquivo.url if c.arquivo else 'Arquivo não enviado',
        ])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=comprovantes.xlsx'
    wb.save(response)
    return response
