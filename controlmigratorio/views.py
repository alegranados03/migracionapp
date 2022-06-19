# Create your views here.
from django.shortcuts import redirect, render
from django.http import HttpResponse
from datetime import date
from .models import Movimiento, Municipio, Departamento, Ciudadano


def index(request):
    movimientos = Movimiento.objects.all()
    return render(request, 'inicio.html', {'movimientos': movimientos})


def registrarMovimiento(request):
    municipios = Municipio.objects.all()
    departamentos = Departamento.objects.all()
    if request.method == 'POST':
        try:
            x = int(request.POST['pasaporte'])
            ciudadano = Ciudadano.objects.get(pasaporte=x)

            Movimiento.objects.create(
                ciudadano=Ciudadano.objects.get(
                    pasaporte=request.POST['pasaporte']),
                tipo_movimiento=request.POST['tipo_movimiento'],
                fecha_movimiento=date.today()
            )
        except:
            Ciudadano.objects.create(
                pasaporte=int(request.POST['pasaporte']),
                primer_nombre=request.POST['primer_nombre'],
                segundo_nombre=request.POST['segundo_nombre'],
                primer_apellido=request.POST['primer_apellido'],
                segundo_apellido=request.POST['segundo_apellido'],
                municipio=Municipio.objects.get(id=request.POST['municipio']),
                alerta_migratoria=False
            )

            Movimiento.objects.create(
                ciudadano=Ciudadano.objects.get(
                    pasaporte=request.POST['pasaporte']),
                tipo_movimiento=request.POST['tipo_movimiento'],
                fecha_movimiento=date.today()
            )

        return redirect('index')
    return render(request, 'registrarMovimiento.html', {'municipios': municipios, 'departamentos': departamentos})


def perfilMigratorio(request, pasaporte_ciudadano):
    ciudadano = Ciudadano.objects.get(pasaporte=pasaporte_ciudadano)
    municipio = Municipio.objects.get(id=ciudadano.municipio_id)
    return render(request, 'perfilMigratorio.html', {'ciudadano': ciudadano, 'municipio': municipio})


def activarAlerta(request, pasaporte):
    ciudadano = Ciudadano.objects.get(pasaporte=pasaporte)
    ciudadano.alerta_migratoria = True
    ciudadano.save()
    return perfilMigratorio(request, ciudadano.pasaporte)


def desactivarAlerta(request, pasaporte):
    ciudadano = Ciudadano.objects.get(pasaporte=pasaporte)
    ciudadano.alerta_migratoria = False
    ciudadano.save()
    return perfilMigratorio(request, ciudadano.pasaporte)


def bucarPerfil(request):
    return render(request, 'buscarPerfil.html')
