from django.db import models

# Create your models here.
class Patientreg(models.Model):
    Name=models.CharField(max_length=30)
    Age=models.IntegerField()
    Gender=models.CharField(max_length=20)
    Address=models.CharField(max_length=100)
    State=models.CharField(max_length=25)
    District=models.CharField(max_length=25)
    Place=models.CharField(max_length=25)
    Email=models.CharField(max_length=25)
    Mobile=models.BigIntegerField()
    Uname=models.CharField(max_length=20)
    Pswd=models.CharField(max_length=15)

class Appointment(models.Model):
    pid=models.IntegerField()
    did=models.IntegerField()
    lid=models.IntegerField()
    spid=models.IntegerField()
    clid=models.IntegerField()
    docid=models.IntegerField()
    Date=models.DateField()
    Time=models.CharField(max_length=20)
    Token=models.IntegerField()
    Status=models.CharField(max_length=20)

class Question(models.Model):
    pid=models.IntegerField()
    Ques=models.CharField(max_length=100)
    Ans=models.CharField(max_length=100)
    Status=models.CharField(max_length=15)

class Suggestion(models.Model):
    pid=models.IntegerField()
    Sugg=models.CharField(max_length=100)
class payment(models.Model):
    uid=models.IntegerField()
    amt=models.IntegerField()

