from django.db import models


# Create your models here.
class Childens(models.Model):
    name =models.CharField(max_length=20,default="")
    rollnumber =models.IntegerField(primary_key=True,default="")
    email=models.EmailField(default="")
    atten=models.IntegerField(default="")
    kannada = models.IntegerField(default="")
    english = models.IntegerField(default="")
    maths = models.IntegerField(default="")
    science = models.IntegerField(default="")
    social = models.IntegerField(default="")
    total = models.IntegerField(default="")