from django.urls import path
from RusticalApp import views

urlpatterns = [
    path("",views.inicio,name='Inicio'),
    path('usuario1/', views.usuario,name='Usuario'),
    path('usuarioApi/', views.usuarioapi),
    path('InteresApi/', views.Interesapi),
    path('Interes1/', views.Interes,name='Interes'),
    path('compra/', views.compra,name='Compra'),
    
]