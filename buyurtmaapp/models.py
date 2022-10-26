from django.core.exceptions import ValidationError
from django.db import models

from userapp.models import Profil
from asosiyapp.models import Mahsulot

def validate_miqdor(value):
    if value >=1 and value <=10:
        return value
    else:
        return ValidationError("Must be between 1 and 10")



class Tanlangan(models.Model):
    profil = models.ForeignKey(Profil,on_delete=models.CASCADE)
    mahsulot = models.ForeignKey(Mahsulot,on_delete=models.CASCADE)

class Savat(models.Model):
    profil = models.ForeignKey(Profil,on_delete=models.CASCADE)
    mahsulot = models.ForeignKey(Mahsulot,on_delete=models.CASCADE)
    miqdor = models.PositiveIntegerField(default=1,validators=[validate_miqdor])
    umumiy = models.PositiveIntegerField()




