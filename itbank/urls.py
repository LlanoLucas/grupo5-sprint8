"""itbank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include

urlpatterns =  [
 path('admin/', admin.site.urls),
 path('registro/', include ('registro.urls'), name='registro'),
 path('clientes/', include('clientes.urls'), name='clientes' ),
path('onlinebanking/', include('clientes.urls'),name='home-clientes'),
 path('prestamos/', include('prestamos.urls'), name='prestamos' ),
 path('sucursales/', include('sucursales.urls'), name='sucursales' ),
 path('VerTarjetas/', include('VerTarjetas.urls'), name='VerTarjetas' ),
 path('PrestamosSucursal/', include('PrestamosSucursal.urls'), name='PrestamosSucursal' ),
 path('SaldoCuenta/', include('SaldoCuenta.urls'), name='SaldoCuenta' ),
 path('SolicitarPrestamo/', include('SolicitarPrestamo.urls'), name='SolicitarPrestamo' ),
 path('direcciones/', include('direcciones.urls'), name='direcciones' ),
 path('',include('home.urls'),name='home')
 ] 