from django.db import models


class EVALUACION(models.Model):
    COD_EVA = models.IntegerField(primary_key=True)
    INSTITUCION = models.CharField(max_length=1)
    MUNICIPIO = models.CharField(max_length=1)
    DETALLE = models.CharField(max_length=1)
    ESTADO = models.CharField(max_length=1)
    
    class Meta:
        db_table = 'EVALUACION'

"""
class seg_permisos(models.Model):
    cod_permisos = models.IntegerField(primary_key=True, default=-1)
    cod_rol = models.IntegerField()
    per_insercion = models.CharField(max_length=1, default=-1)
    per_eliminar = models.CharField(max_length=1, default=-1)
    per_actualizar = models.CharField(max_length=1, default=-1)
    per_consultar = models.CharField(max_length=1, default=-1)
    fec_modificacion = models.DateTimeField(default=timezone.now)

    #
    class Meta:
        db_table = 'seg_permisos'

"""