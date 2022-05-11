from django.db import models

# Create your models here.

class Padre(models.Model):
    nombre=models.CharField(max_length=50)
    edad=models.IntegerField()
    type = "padre"

    def __str__(self):
        return self.nombre+" "+str(self.edad)

class Madre(models.Model):
    nombre=models.CharField(max_length=50)
    edad=models.IntegerField()
    type = "madre"

    def __str__(self):
        return self.nombre+" "+str(self.edad)

class Hermano(models.Model):
    nombre=models.CharField(max_length=50)
    edad=models.IntegerField()
    type = "hermano"

    def __str__(self):
        return self.nombre+" "+str(self.edad)