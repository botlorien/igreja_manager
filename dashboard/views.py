from django.shortcuts import render, get_object_or_404
from igrejas.models import Igreja
from membros.models import Membro
from comprovantes.models import Comprovante
from django.db.models import Sum, Count
from datetime import datetime
import calendar
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_igreja(request, igreja_id):
    igreja = get_object_or_404(Igreja, id=igreja_id)
    membros = Membro.objects.filter(igreja=igreja)

    # Faturamento mensal
    labels = []
    valores = []

    for mes in range(1, 13):
        labels.append(calendar.month_abbr[mes])
        total = Comprovante.objects.filter(
            membro__in=membros,
            data_comprovante__month=mes
        ).aggregate(Sum('valor'))['valor__sum'] or 0
        valores.append(float(total))

    # Membros recorrentes = membros com mais de 3 comprovantes no ano
    ano = datetime.now().year
    recorrentes = Comprovante.objects.filter(
        membro__in=membros,
        data_comprovante__year=ano
    ).values('membro').annotate(qtd=Count('id')).filter(qtd__gte=3).count()

    return render(request, 'dashboard/dashboard.html', {
        'igreja': igreja,
        'labels': labels,
        'valores': valores,
        'recorrentes': recorrentes,
        'total_membros': membros.count(),
    })
