from django import forms
from .models import Comprovante

class ComprovanteForm(forms.ModelForm):
    class Meta:
        model = Comprovante
        fields = ['membro', 'valor', 'tipo', 'data_comprovante', 'arquivo']
        widgets = {
            'data_comprovante': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'membro': forms.Select(attrs={'class': 'form-select'}),
            'arquivo': forms.FileInput(attrs={'class': 'form-control'}),
        }
