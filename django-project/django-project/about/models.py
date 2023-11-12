from django.db import models

class Santri(models.Model):
  NAMA           = models.CharField(max_length=255)
  NIM            = models.IntegerField(null=True)
  TANGGAL_LAHIR  = models.DateField(null=True)
  ALAMAT_TINGGAL = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.Nama}"
  
class Member(models.Model):
  NAMA          = models.CharField(max_length=255)
  ALAMAT_TINGGAL= models.TextField()
  TANGGAL_LAHIR = models.CharField(max_length=255)


  def __str__(self):
    return f"{self.Nama}"