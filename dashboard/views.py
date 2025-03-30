from django.shortcuts import render, get_object_or_404
from igrejas.models import Igreja
from membros.models import Membro
from comprovantes.models import Comprovante
from django.db.models import Sum, Count
from datetime import datetime
import calendar
from django.contrib.auth.decorators import login_required
from django.db.models.functions import TruncMonth
from django.utils.dateparse import parse_date

@login_required
def dashboard_igreja(request, igreja_id):
    igreja = get_object_or_404(Igreja, id=igreja_id)
    membros = Membro.objects.filter(igreja=igreja)

    # 🔎 Filtros GET
    membro_id = request.GET.get('membro')
    tipo = request.GET.get('tipo')

    comprovantes = Comprovante.objects.filter(membro__igreja=igreja)

    if membro_id:
        comprovantes = comprovantes.filter(membro_id=membro_id)

    if tipo:
        comprovantes = comprovantes.filter(tipo=tipo)

    # Faturamento total
    total_faturamento = comprovantes.aggregate(total=Sum('valor'))['total'] or 0

    # Faturamento por mês (com filtros aplicados)
    por_mes = comprovantes.annotate(
        mes=TruncMonth('data_comprovante')
    ).values('mes').annotate(
        total=Sum('valor')
    ).order_by('mes')

    labels = [m['mes'].strftime('%b') for m in por_mes]
    valores = [float(m['total']) for m in por_mes]

    # Membros recorrentes
    ano = datetime.now().year
    recorrentes = Comprovante.objects.filter(
        membro__in=membros,
        data_comprovante__year=ano
    ).values('membro').annotate(qtd=Count('id')).filter(qtd__gte=2).count()

    return render(request, 'dashboard/dashboard.html', {
        'igreja': igreja,
        'membros': membros,
        'labels': labels,
        'valores': valores,
        'recorrentes': recorrentes,
        'total_membros': membros.count(),
        'total_faturamento': total_faturamento,
        'filtros': {
            'membro_id': membro_id,
            'tipo': tipo,
        }
    })
