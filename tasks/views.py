from django.shortcuts import render, redirect
# agregamos redirect para redirecionar vistas
# importamos la creacion del formuario desde django
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# importamos la creacion de user
from django.contrib.auth.models import User
# import para crear coki
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserForm , AgendarForm
from django.http import HttpResponse
from django.urls import reverse
from tasks.models import Producto
from tasks.Carrito import Carrito



# Create your views here.

def home(request):
    # llamar las hojas html por medio del render
    return render(request, 'home.html')


def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form':CustomUserForm()
        })

    else:
        if request.POST['password1'] == request.POST['password2']:
            # registro user
            try:
                # guardar usuario y madarlo a otro lado
                user = User.objects.create_user(
                    first_name=request.POST['first_name'],last_name=request.POST['last_name'],
                    email=request.POST['email'],username=request.POST['username'],
                    password=request.POST['password1'])
                user.save()
                # mostar el usuario con cokis
                login(request, user)
                return redirect('home')
            except:
                return render(request, 'signup.html', {
                    'form': CustomUserForm(),
                    'error': 'usuario ya existe '
                })

        return render(request, 'signup.html', {
            'form': CustomUserForm(),
            'error': 'contraseñas no son iguales'
        })


# cerrar las seciones#


def signout(request):
    logout(request)
    return redirect('home')

# login revision si existe y delvuelve


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user= authenticate(request, username=request.POST['username'],password=request.POST
                    ['password'])
        if user is None:
            return render(request, 'signin.html', {
            'form': AuthenticationForm,
            'error': 'su usuario o contraseña es incorrecto'
        })
        else:
            login(request, user)
            return redirect('home')
        
# agendamiento 

def agendar_hora (request):
    agendar_form = AgendarForm()

    if request.method == "POST":
        agendar_form = AgendarForm(data=request.POST)
        if agendar_form.is_valid():
            agendar_form.save()
            name = request.POST.get('name', '')
            apaterno = request.POST.get('apaterno', '')
            amaterno = request.POST.get('amaterno', '')
            correo = request.POST.get('correo', '')
            hora = request.POST.get('hora', '')
            comentario = request.POST.get('comentario', '')   
            return redirect(reverse('agendar_hora')+"?ok")
        

    return render(request, "agendar_hora.html", {'form': agendar_form} )

#carrito de compra

def compra(request):
    return render(request, 'compra.html', {})

def tienda(request):
    productos = Producto.objects.all()
    return render(request, "tienda.html", {'productos':productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("tienda")
    

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("tienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("tienda")


def hombre(request):
    return render(request, "carrusel.html")

def mujer(request):
    return render(request, "carruselmujer.html")

def nino(request):
    return render(request, "carruselninos.html")


