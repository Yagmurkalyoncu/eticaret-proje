from django.urls import path
from . import views

urlpatterns = [
    path('', views.anasayfa, name='anasayfa'),
    path('urun/<int:pk>/', views.urun_detay, name='urun_detay'),
    path('siparis/<int:pk>/', views.siparis_ver, name='siparis_ver'),
    path('basarili/', views.siparis_basarili, name='siparis_basarili'),
]