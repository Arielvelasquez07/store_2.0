from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ContactoForm
from .models import Contacto,Categoria,Pelicula,Carrito, CarritoItem

def index(request):
    return render(request, 'index.html')

def contacto(request):
    return render(request, 'contacto.html')

def contacto_nuevo(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacto_confirmacion')
    else:
        form = ContactoForm()
    return render(request, 'myportfolio/contacto_formulario.html', {'form': form})


def contacto_detalle(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    return render(request, 'myportfolio/contacto_detalle.html', {'contacto': contacto})

def contacto_editar(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    if request.method == "POST":
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid():
            form.save()
            return redirect('contacto_detalle', pk=contacto.pk)
    else:
        form = ContactoForm(instance=contacto)
    return render(request, 'myportfolio/contacto_editar.html', {'form': form})


def contacto_eliminar(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    contacto.delete()
    return redirect('contacto_lista')

def contacto_lista(request):
    contactos = Contacto.objects.all()
    return render(request, 'myportfolio/contacto_lista.html', {'contactos': contactos})

def contacto_confirmacion(request):
    return render(request, 'myportfolio/contacto_confirmacion.html') 

def catalogo_view(request):
    categorias = Categoria.objects.all()
    peliculas = Pelicula.objects.all()
    context = {
        'categorias': categorias,
        'peliculas': peliculas
    }
    return render(request, 'index.html', context)

def agregar_al_carrito(request, pelicula_id):
    pelicula = get_object_or_404(Pelicula, id=pelicula_id)
    carrito, created = Carrito.objects.get_or_create(user=request.user)
    
    carrito_item, created = CarritoItem.objects.get_or_create(carrito=carrito, pelicula=pelicula)
    if not created:
        carrito_item.cantidad += 1
        carrito_item.save()

    return redirect('nombre_de_la_vista')


def ver_carrito(request):
    carrito = Carrito.objects.get(user=request.user)
    return render(request, 'carrito.html', {'carrito': carrito})


