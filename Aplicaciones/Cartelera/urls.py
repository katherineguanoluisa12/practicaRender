from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path ('listadoGeneros/',views.listadoGeneros,name='listadoGeneros'),
    path ('listadoDirector/',views.listadoDirector,name='listadoDirector'),
    path ('listadoPais/',views.listadoPais,name='listadoPais'),
    path ('listadoPeliculas/',views.listadoPelicula,name='listadoPeliculas'),
    path('eliminarGenero/<id>',views.eliminarGenero,name='eliminarGenero'),
    path('eliminarPelicula/<id>',views.eliminarPelicula,name='eliminarPelicula'),
    path('eliminarPais/<id>',views.eliminarPais,name='eliminarPais'),
    path('nuevoGenero/',views.nuevoGenero,name='nuevoGenero'),
    path('guardarGenero/',views.guardarGenero,name='guardarGenero'),
    path('editarGenero/<id>',views.editarGenero,name='editarGenero'),
    path('procesarActualizacionGenero/',views.procesarActualizacionGenero,name='procesarActualizacionGenero'),
    path('nuevoPais/',views.nuevoPais,name='nuevoPais'),
    path('guardarPais/',views.guardarPais,name='guardarPais'),
    path('editarPais/<id>',views.editarPais,name='editarPais'),
    path('procesarActualizacionPais/',views.procesarActualizacionPais,name='procesarActualizacionPais'),
    
    path('eliminarDirector/<id>',views.eliminarDirector,name='eliminarDirector'),
    path('nuevoDirector/',views.nuevoDirector,name='nuevoDirector'),
    path('guardarDirector/',views.guardarDirector,name='guardarDirector'),
    path('editarDirector/<id>',views.editarDirector,name='editarDirector'),
    path('procesarActualizacionDirector/',views.procesarActualizacionDirector,name='procesarActualizacionDirector'),
    
    path('nuevoPelicula/',views.nuevoPelicula,name='nuevoPelicula'),
    path('guardarPelicula/',views.guardarPelicula,name='guardarPelicula'),
    path('editarPelicula/<id>',views.editarPelicula,name='editarPelicula'),
    path('procesarActualizacionPelicula/',views.procesarActualizacionPelicula,name='procesarActualizacionPelicula'),
    path('gestionCines/',views.gestionCines, name='gestionCines'), 
    path('insertarCine/',views.insertarCine,name='insertarCine'),
    path('listadoCines/',views.listadoCines,name='listadoCines'),
    path('gestionarDirectores/',views.gestionarDirectores, name='gestionarDirectores'), 
    path('listadoDirectores/',views.listadoDirectores, name='listadoDirectores'), 
    path('agregarDirector/',views.agregarDirector,name='agregarDirector'),
#PELICULAS
     path('gestionPeliculas/',views.gestionPeliculas, name='gestionPeliculas'), 
     path('guardarPelicula/',views.guardarPelicula, name='guardarPelicula'), 
     path('listadoPeliculas/',views.listadoPeliculas, name='listadoPeliculas'), 
    #  path('exportsCinesPDF/',views.exportsCinesPDF, name='exportsCinesPDF'), 
]
    

    
    

    
    
    
    
    
    
    
