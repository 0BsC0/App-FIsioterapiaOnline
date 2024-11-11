from django.contrib import admin
from django.urls import path, include
from .views import bienvenida

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bienvenida, name='bienvenida'),
    path('', include('autenticacion.urls')), 
]
