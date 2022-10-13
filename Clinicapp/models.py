from django.db import models

# Create your models here.
class ClinicReg(models.Model):
    Name=models.CharField(max_length=30)
    Contact=models.BigIntegerField()
    Owner=models.CharField(max_length=50)
    OwnerContact=models.BigIntegerField()
    Address=models.CharField(max_length=100)
    Email=models.CharField(max_length=25)
    District=models.CharField(max_length=25)
    Place=models.CharField(max_length=25)
    Location=models.CharField(max_length=50)
    Uname=models.CharField(max_length=20)
    Pswd=models.CharField(max_length=15)
    Status=models.CharField(max_length=15,default='pending')

class Clinicdet(models.Model):
    sid=models.IntegerField()
    did = models.IntegerField()
    pid = models.IntegerField()
    clid = models.IntegerField()
    spid = models.IntegerField()
    Photo=models.FileField(upload_to='file')


