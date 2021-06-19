from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('crear/barrio', views.crear_barrio,
         name='crearBarrio'),
    path('barrio/<int:id>', views.editar_barrio,
         name='editarBarrio'),
    path('crear/parroquia', views.crear_parroquia,
         name='crearParroquia'),
    path('parroquia/<int:id>', views.editar_parroquia,
         name='editarParroquia'),
    path('barrios', views.listar_barrio,
         name='listarBarrios'),
]