from django import forms
from .models import Comprovante
from membros.models import Membro

class ComprovanteForm(forms.ModelForm):
    class Meta:
        model = Comprovante
        fields = ['membro', 'valor', 'tipo', 'data_comprovante', 'arquivo']
        widgets = {
            'data_comprovante': forms.DateInput(format='%Y-%m-%d', attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'membro': forms.Select(attrs={'class': 'form-select'}),
            'arquivo': forms.FileInput(attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        igreja = kwargs.pop('igreja', None)
        super().__init__(*args, **kwargs)

        # ⚠️ Isso é crucial para funcionar corretamente com type=date
        self.fields['data_comprovante'].input_formats = ['%Y-%m-%d']
        
        if igreja:
            self.fields['membro'].queryset = Membro.objects.filter(igreja=igreja)
