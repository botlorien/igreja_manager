import django_filters
from .models import Comprovante
from membros.models import Membro

class ComprovanteFilter(django_filters.FilterSet):
    data_inicio = django_filters.DateFilter(field_name='data_comprovante', lookup_expr='gte', label="De")
    data_fim = django_filters.DateFilter(field_name='data_comprovante', lookup_expr='lte', label="Até")
    membro = django_filters.ModelChoiceFilter(queryset=Membro.objects.all())
    tipo = django_filters.ChoiceFilter(choices=[('D', 'Dízimo'), ('O', 'Oferta')])

    class Meta:
        model = Comprovante
        fields = ['membro', 'tipo', 'data_inicio', 'data_fim']
