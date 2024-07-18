from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogo_view, name='home'),  
    path('contacto/', views.contacto, name='contacto'),
    path('contacto/nuevo/', views.contacto_nuevo, name='contacto_nuevo'),
    path('contacto/<int:pk>/', views.contacto_detalle, name='contacto_detalle'),
    path('contacto/<int:pk>/editar/', views.contacto_editar, name='contacto_editar'),
    path('contacto/<int:pk>/eliminar/', views.contacto_eliminar, name='contacto_eliminar'),
    path('contacto/', views.contacto_lista, name='contacto_lista'),
    path('contacto/confirmacion/', views.contacto_confirmacion, name='contacto_confirmacion'),
    path('', views.index, name='index'), 


]
