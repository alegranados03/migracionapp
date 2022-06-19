from django.db import models
from enum import Enum

 
class MovimientoEnum(Enum):
    SA = 'Salida del país'
    IN = 'Ingreso al país'

class Departamento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_departamento = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ['id']


class Municipio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_municipio = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento, on_delete=models.RESTRICT)

    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'
        ordering = ['id']


class Ciudadano(models.Model):
    pasaporte = models.IntegerField(primary_key=True)
    primer_nombre = models.CharField(max_length=300)
    segundo_nombre = models.CharField(max_length=300)
    primer_apellido = models.CharField(max_length=300)
    segundo_apellido = models.CharField(max_length=300)
    municipio = models.ForeignKey(Municipio, on_delete=models.RESTRICT)
    alerta_migratoria = models.BooleanField(default = False)


    class Meta:
        verbose_name = 'Ciudadano'
        verbose_name_plural = 'Ciudadanos'
        ordering = ['pasaporte']

class Movimiento(models.Model):
    id = models.AutoField(primary_key=True)
    ciudadano = models.ForeignKey(Ciudadano, on_delete=models.RESTRICT)
    tipo_movimiento =models.CharField(max_length=5,choices=[(tag, tag.value) for tag in MovimientoEnum])
    fecha_movimiento = models.DateField()

    class Meta:
        verbose_name = 'Movimiento'
        verbose_name_plural = 'Movimientos'
        ordering = ['id']


