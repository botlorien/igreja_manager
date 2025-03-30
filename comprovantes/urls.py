from django.urls import path
from . import views

app_name = 'comprovantes'

urlpatterns = [
    path('<int:igreja_id>/', views.lista_comprovantes, name='lista'),
    path('novo/<int:igreja_id>/', views.adicionar_comprovante, name='novo'),
    path('editar/<int:pk>/', views.editar_comprovante, name='editar'),

    path('ver/<int:pk>/', views.visualizar_comprovante, name='visualizar'),
    path('exportar/<int:igreja_id>/', views.exportar_excel, name='exportar_excel'),
]
