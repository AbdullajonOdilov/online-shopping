from django.contrib.auth.models import User
from django.db import models

class Profil(models.Model):
    shahar = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)
    jins = models.CharField(max_length=10, choices=[("Erkak","Erkak"),("Ayol","Ayol")])
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):f"{self.user.first_name}, {self.user.lasr_name}"
