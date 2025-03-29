from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('<int:igreja_id>/', views.dashboard_igreja, name='painel'),
]
