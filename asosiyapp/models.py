from django.db import models

# Create your models here.

class Bolim(models.Model):
    nom = models.CharField(max_length=30)
    rasm = models.FileField(upload_to='bolimlar')
    def __str__(self):
        return self.nom

class Ichki(models.Model):
    nom = models.CharField(max_length=30)
    rasm = models.FileField(upload_to='ichki_bolimlar')
    bolim = models.ForeignKey(Bolim, on_delete=models.CASCADE, related_name='ichkilari')
    def __str__(self):
        return self.nom
class Mahsulot(models.Model):
    nom = models.CharField(max_length=30)
    brend = models.CharField(max_length=20)
    narx = models.FloatField()
    batafsil = models.TextField()
    kafolat = models.CharField(max_length=30)
    yetkazish = models.CharField(max_length=20)
    mavjud = models.BooleanField()
    chegirma = models.FloatField(default=0)
    ichki = models.ForeignKey(Ichki,on_delete=models.CASCADE)
    def __str__(self):return self.nom
class Rasm(models.Model):
    rasm = models.FileField(upload_to='ichki_mahsulot')
    mahsulot = models.ForeignKey(Mahsulot,on_delete=models.CASCADE,related_name='rasmlari')
