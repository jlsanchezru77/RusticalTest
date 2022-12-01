from django.shortcuts import render
from django.http import HttpResponse

from RusticalApp.models import usuario1
from RusticalApp.models import Interes1
from RusticalApp.models import compra1
from django.core import serializers

from RusticalApp.forms import UsuarioFormulario
from RusticalApp.forms import CompraFormulario
from RusticalApp.forms import InteresFormulario



def inicio(request):
    return render(request,'RusticalApp/inicio.html')

def usuario(request):
    if request.method == "POST":
        miFormulario = UsuarioFormulario(request.POST) # Aqui me llega la informacion del html            
        print(miFormulario)               
    
        if miFormulario.is_valid:                   
             informacion = miFormulario.cleaned_data                   
             familia = usuario1(Nombre=informacion["Nombre"], Apellidos=informacion["Apellidos"], Edad=informacion["Edad"])                  
             familia.save()                   
             return render(request, "RusticalApp/inicio.html")       
    else:             
        miFormulario = UsuarioFormulario()
 
    return render(request, "RusticalApp/usuario.html", {"miFormulario": miFormulario})
           


def Interes(request):
    if request.method == "POST":
        miFormulario = InteresFormulario(request.POST) # Aqui me llega la informacion del html            
        print(miFormulario)               
    
        if miFormulario.is_valid:                   
             informacion = miFormulario.cleaned_data                   
             familia2 = Interes1(status=informacion["status"])                  
             familia2.save()                   
             return render(request, "RusticalApp/inicio.html")       
    else:             
        miFormulario = InteresFormulario()
 
    return render(request, "RusticalApp/interes.html", {"miFormulario": miFormulario})
    

   
    

def compra(request):
    if request.method == "POST":
        miFormulario1 = CompraFormulario(request.POST) # Aqui me llega la informacion del html            
        print(miFormulario1)               
    
        if miFormulario1.is_valid:                   
             informacion = miFormulario1.cleaned_data                   
             familia1 = compra1(Peso=informacion["Peso"], Unidades=informacion["Unidades"])                  
             familia1.save()                   
             return render(request, "RusticalApp/inicio.html")       
    else:             
        miFormulario1 = CompraFormulario()
 
    return render(request, "RusticalApp/compra.html", {"miFormulario1": miFormulario1})
    

def usuarioapi(request):
    usuario_todos=usuario1.objects.all()
    return HttpResponse(serializers.serialize('json',usuario_todos))     #Esto lo vuelve tipo diccionario
def Interesapi(request):
    Interes_todos=Interes1.objects.all()
    return HttpResponse(serializers.serialize('json',Interes_todos))    

       