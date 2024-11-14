from django.shortcuts import render


def bienvenida(request):
    return render(request, 'bienvenida/bienvenida.html')




