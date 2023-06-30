"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from tasks.views import agregar_producto,eliminar_producto,restar_producto,limpiar_carrito, tienda,compra


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('signup/', views.signup,name='signup'),
    path('agendar/', views.agendar_hora ,name='agendar'),
    path('logout/', views.signout, name='logout' ),
    path('signin/', views.signin, name='signin' ),
    path('agendar_hora/', views.agendar_hora, name="agendar_hora"),

    path('tienda/', tienda, name="tienda"),
    path('compra/', compra),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"), 
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"), 
    path('restar/<int:producto_id>/', restar_producto, name="Sub"), 
    path('limpiar/', limpiar_carrito, name="CLS"), 

    path('hombres/', views.hombre, name='hombres'),
    path('mujeres/', views.mujer, name='mujeres'),
    path('ninos/', views.nino, name='ninos'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


