from django.urls import path
from . import views

app_name = 'membros'

urlpatterns = [
    path('<int:igreja_id>/', views.lista_membros, name='lista'),
    path('criar/', views.MembroCreateView.as_view(), name='criar'),
]
