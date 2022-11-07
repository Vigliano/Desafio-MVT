from django.shortcuts import render

# Create your views here.

from MiApp.models import Familiares

def mostrar_familiares(request):

    f1 = Familiares(nombre ='Sancho Panza', edad=32, cumpleanios='1991-10-27')
    f2 = Familiares(nombre ='Martin Fierro', edad=45, cumpleanios='1977-11-15')
    f3 = Familiares(nombre ='Viejo Vizcacha', edad=62, cumpleanios='1960-12-20')
    
    return render(request, 'MiApp/familia.html', {'familia':[f1,f2,f3]})