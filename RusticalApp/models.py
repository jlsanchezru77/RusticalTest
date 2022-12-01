from django.db import models
from model_utils import Choices
from django.utils.translation import gettext as _


class usuario1(models.Model):
    Nombre=models.CharField(max_length=40)
    Apellidos=models.CharField(max_length=40)
    Edad=models.IntegerField()

class Interes1(models.Model):
    STATUS=Choices(
        ('Compra', _('Me interesa adquirir Orellanas')),
        ('Cultivo', _('Me interesa cultivar Orellanas')),
    )     
    # [..]
    status=models.CharField(
        max_length=32,
        choices=STATUS,
        #default=STATUS.Compra,

    )

class compra1(models.Model):
    Peso=models.IntegerField()
    Unidades=models.IntegerField()      
    
