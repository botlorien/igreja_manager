from django.urls import path
from . import views

app_name = 'igrejas'

urlpatterns = [
    path('', views.igreja_list_view, name='lista'),
    path('<int:igreja_id>/', views.igreja_detail_view, name='detalhe'),
    path('criar/', views.IgrejaCreateView.as_view(), name='criar'),
]
