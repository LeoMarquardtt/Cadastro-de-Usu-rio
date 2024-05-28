from django.urls import path, include
from app_cad_usuarios import views


urlpatterns = [
    path('', views.home, name='home'),
    path('salvar/', views.salvar, name='salvar'),
    path('atualizar/<int:id>/', views.atualizar, name='atualizar'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
]
