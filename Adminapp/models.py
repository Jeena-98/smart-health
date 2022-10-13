from django.db import models

# Create your models here.
class Login(models.Model):
    Uname=models.CharField(max_length=30)
    Pswd=models.CharField(max_length=20)
    Utype=models.CharField(max_length=20)

class State(models.Model):
    State=models.CharField(max_length=30)

class District(models.Model):
    sid=models.IntegerField()
    district=models.CharField(max_length=30)

class Place(models.Model):
    sid=models.IntegerField()
    did=models.IntegerField()
    Place=models.CharField(max_length=30)

class Specialization(models.Model):
    Category=models.CharField(max_length=50)
class Bank(models.Model):
    bname=models.CharField(max_length=50)
    logo=models.ImageField(upload_to="logo")
class Branch(models.Model):
    branch=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    ifsc=models.CharField(max_length=50)
    phone=models.BigIntegerField()
    email=models.CharField(max_length=50)
    bname=models.IntegerField()
class Account(models.Model):
    cname=models.CharField(max_length=50)
    cno=models.BigIntegerField()
    cvv=models.IntegerField()
    year=models.IntegerField()
    month=models.IntegerField()
    amount=models.BigIntegerField()
    bname=models.IntegerField()
    branch=models.IntegerField()