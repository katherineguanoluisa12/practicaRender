import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Cine, Genero, Director, Pais, Pelicula
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, "home.html")

def listadoGeneros(request):
    generosBdd = Genero.objects.all()
    return render(request, "listadoGeneros.html", {'generos': generosBdd})

def listadoDirector(request):
    directorBdd = Director.objects.all()
    return render(request, "listadoDirector.html", {'directores': directorBdd})

def listadoPais(request):
    paisBdd = Pais.objects.all()
    return render(request, "listadoPais.html", {'paises': paisBdd})

def listadoPelicula(request):
    peliculaBdd = Pelicula.objects.all()
    return render(request, "listadoPeliculas.html", {'peliculas': peliculaBdd})

def eliminarGenero(request, id):
    generoEliminar = Genero.objects.get(id=id)
    generoEliminar.delete()
    messages.success(request, "Genero Eliminado correctamente.")
    return redirect('listadoGeneros')

def eliminarPelicula(request, id):
    peliculaEliminar = Pelicula.objects.get(id=id)
    peliculaEliminar.delete()
    messages.success(request, "Pelicula Eliminada correctamente.")
    return redirect('listadoPeliculas')

def eliminarPais(request, id):
    paisEliminar = Pais.objects.get(id=id)
    paisEliminar.delete()
    messages.success(request, "Pais Eliminado correctamente.")
    return redirect('listadoPais')

def eliminarDirector(request, id):
    directorEliminar = Director.objects.get(id=id)
    directorEliminar.delete()
    messages.success(request, "Director Eliminado correctamente.")
    return redirect('listadoDirector')

def nuevoGenero(request):
    return render(request, 'nuevoGenero.html')

def guardarGenero(request):
    nom = request.POST["nombre"]
    des = request.POST["descripcion"]
    fot = request.FILES.get('foto')
    nuevoGenero = Genero.objects.create(nombre=nom, descripcion=des,foto=fot)
    messages.success(request, "Genero registrado correctamente.")
    return redirect('listadoGeneros')


def editarGenero(request, id):
    generoEditar = Genero.objects.get(id=id)
    return render(request, 'editarGenero.html', {'generoEditar': generoEditar})

def procesarActualizacionGenero(request):
    id = request.POST['id']
    nombre = request.POST['nombre']
    descripcion = request.POST['descripcion']

    generoConsultado = Genero.objects.get(id=id)
    generoConsultado.nombre = nombre
    generoConsultado.descripcion = descripcion
    generoConsultado.save()
    messages.success(request, 'Genero actualizado exitosamente')
    return redirect('listadoGeneros')

def nuevoPais(request):
    return render(request, 'nuevoPais.html')

def guardarPais(request):
    nom = request.POST["nombre"]
    con = request.POST["continente"]
    cap = request.POST["capital"]
    nuevoPais = Pais.objects.create(nombre=nom, continente=con, capital=cap)
    messages.success(request, "Pais registrado correctamente.")
    return redirect('listadoPais')

def editarPais(request, id):
    paisEditar = Pais.objects.get(id=id)
    return render(request, 'editarPais.html', {'paisEditar': paisEditar})

def procesarActualizacionPais(request):
    id = request.POST['id']
    nombre = request.POST['nombre']
    continente = request.POST['continente']
    capital = request.POST['capital']

    paisConsultado = Pais.objects.get(id=id)
    paisConsultado.nombre = nombre
    paisConsultado.continente = continente
    paisConsultado.capital = capital
    paisConsultado.save()
    messages.success(request, 'Pais actualizado exitosamente')
    return redirect('listadoPais')

def nuevoDirector(request):
    return render(request, 'nuevoDirector.html')

def guardarDirector(request):
    dni = request.POST["dni"]
    nom = request.POST["nombre"]
    ape = request.POST["apellido"]
    est = 'estado' in request.POST
    fot = request.FILES.get("foto")
    nuevoDirector = Director.objects.create(dni=dni, nombre=nom, apellido=ape, estado=est, foto=fot)
    messages.success(request, "Director registrado correctamente.")
    return redirect('listadoDirector')

def editarDirector(request, id):
    directorEditar = Director.objects.get(id=id)
    return render(request, 'editarDirector.html', {'directorEditar': directorEditar})

def procesarActualizacionDirector(request):
    id = request.POST['id']
    dni = request.POST['dni']
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    estado = 'estado' in request.POST

    directorConsultado = Director.objects.get(id=id)
    directorConsultado.dni = dni
    directorConsultado.nombre = nombre
    directorConsultado.apellido = apellido
    directorConsultado.estado = estado
    directorConsultado.save()
    messages.success(request, 'Director actualizado exitosamente')
    return redirect('listadoDirector')

def nuevoPelicula(request):
    context = {
        'generos': Genero.objects.all(),
        'directores': Director.objects.all(),
        'paises': Pais.objects.all()
    }
    return render(request, 'nuevoPelicula.html', context)

def guardarPelicula(request):
    titulo = request.POST["titulo"]
    duracion = request.POST["duracion"]
    sinopsis = request.POST["sinopsis"]
    genero_id = request.POST["genero"]
    director_id = request.POST["director"]
    pais_id = request.POST["pais"]

    genero = Genero.objects.get(id=genero_id)
    director = Director.objects.get(id=director_id)
    pais = Pais.objects.get(id=pais_id)

    nuevoPelicula = Pelicula.objects.create(
        titulo=titulo,
        duracion=duracion,
        sinopsis=sinopsis,
        genero=genero,
        director=director,
        pais=pais
    )
    messages.success(request, "Pelicula registrada correctamente.")
    return redirect('listadoPeliculas')

def editarPelicula(request, id):
    peliculaEditar = Pelicula.objects.get(id=id)
    context = {
        'peliculaEditar': peliculaEditar,
        'generos': Genero.objects.all(),
        'directores': Director.objects.all(),
        'paises': Pais.objects.all()
    }
    return render(request, 'editarPelicula.html', context)

def procesarActualizacionPelicula(request):
    id = request.POST['id']
    titulo = request.POST["titulo"]
    duracion = request.POST["duracion"]
    sinopsis = request.POST["sinopsis"]
    genero_id = request.POST["genero"]
    director_id = request.POST["director"]
    pais_id = request.POST["pais"]

    genero = Genero.objects.get(id=genero_id)
    director = Director.objects.get(id=director_id)
    pais = Pais.objects.get(id=pais_id)

    peliculaConsultado = Pelicula.objects.get(id=id)
    peliculaConsultado.titulo = titulo
    peliculaConsultado.duracion = duracion
    peliculaConsultado.sinopsis = sinopsis
    peliculaConsultado.genero = genero
    peliculaConsultado.director = director
    peliculaConsultado.pais = pais

    peliculaConsultado.save()
    messages.success(request, 'Pelicula actualizada exitosamente')
    return redirect('listadoPeliculas')

#FUncion para gestionar Crud de Cine
def gestionCines (request):
    return render (request,'gestionCines.html')


@csrf_exempt
def insertarCine(request):
    nom = request.POST["nombre"]
    dir = request.POST["direccion"]
    tel = request.POST["telefono"]
    nuevoCine = Cine.objects.create(nombre=nom, direccion=dir, telefono=tel)
    return JsonResponse({ 
                         
    'estado': True,
    'mensaje':'Cine Registrado exitosamente',
    })
    
#Renderizar el listado Cines
def listadoCines(request):
    cines = Cine.objects.all()
    return render(request, "listadoCines.html", {'cines': cines})    

# Directores

def gestionarDirectores(request):
    return render(request,'director/gestionarDirector.html')

def listadoDirectores(request):
    director = Director.objects.all()
    return render(request, "director/listadoDirectores.html", {'directores': director})  
#Agregar Director con fetch
@csrf_exempt
def agregarDirector(request):
    dni = request.POST["dni"]
    nombre = request.POST["nombre"]
    apellido = request.POST["apellido"]
    estado = request.POST.get("estado") == 'on'
    foto = request.FILES.get("foto")
    
    nuevoDirector = Director.objects.create(dni=dni,nombre=nombre,apellido=apellido,estado=estado,foto=foto)
    
    return JsonResponse({
        'estado': True,
        'mensaje': 'Director registrado exitosamente',
    })
    
#PELICULA
def gestionPeliculas(request):
    director = Director.objects.all()
    genero = Genero.objects.all()
    return render(request,'gestionPelicula.html',{'directores':director,'generos':genero})

#Insertando cines mediante AJAX en la Base de Datos
@csrf_exempt
def guardarPelicula(request):
    tit = request.POST["titulo"]
    dur = request.POST["duracion"]
    sip = request.POST["sinopsis"]

    gen = request.POST["genero"]
    genero_instancia = Genero.objects.get(id=gen)

    dir = request.POST["director"]
    director_instancia = Director.objects.get(id=dir)

    nuevaPelicula = Pelicula.objects.create(
        titulo=tit, duracion=dur, sinopsis=sip,
        genero=genero_instancia, director=director_instancia
    )

    return JsonResponse({
        'estado': True,
        'mensaje': 'Película registrada exitosamente.'
    })

    

def listadoPeliculas(request):
    peliculasBdd=Pelicula.objects.all()
    return render(request,"listadoPelicula.html", {'peliculas':peliculasBdd})

# def exportCinesPDF(request):
#     #llamar a todos los datos del modelo cina
#     cines = Cine.objects.all()
#     #llamar al template con el render string
#     html_string = render_to_string('exportCines.html', {'cines': cines})
#     #almacenar como un archivo html
#     html = HTML(string=html_string)
#     #leer todo el html guardado y convvertirlo en un pd
#     # f
#     pdf = html.write_pdf()
#     #dar una respuesta como pdf(archivo)
#     response = HttpResponse(pdf, content_type='application/pdf')
#     #nombrar y dar una extension al archivo expotado
#     response['Content-Disposition'] = 'attachment; filename="reporte_cines.pdf"'
#     #exportar archivo
#     return response