from django.db import models

# Create your models here.
class Doctorreg(models.Model):
    clid=models.IntegerField()
    DrName=models.CharField(max_length=20)
    License=models.CharField(max_length=20)
    Age=models.IntegerField()
    Gender=models.CharField(max_length=20)
    Qualification=models.CharField(max_length=30)
    Specialization=models.CharField(max_length=20,default='')
    Mobile=models.BigIntegerField()
    Email=models.CharField(max_length=25)
    Uname=models.CharField(max_length=25)
    Pwd=models.CharField(max_length=25)
    Status=models.CharField(max_length=20)

class Medihis(models.Model):
    pid=models.IntegerField()
    docid=models.IntegerField(default=1)
    Bgroup=models.CharField(max_length=10)
    Height=models.IntegerField()
    Weight=models.ImageField()
    Physician=models.CharField(max_length=25)
    Smoke=models.CharField(max_length=20)
    Drink=models.CharField(max_length=20)
    Disease=models.CharField(max_length=20)
    Reaction=models.CharField(max_length=20)
    Medicine=models.CharField(max_length=20)
    Dosage=models.IntegerField()
    Purpose=models.CharField(max_length=30)
    Diabetic=models.CharField(max_length=20,default='')
    Sugar=models.CharField(max_length=20)
    Allergy=models.CharField(max_length=20)
    Family=models.CharField(max_length=20)
    Immunity=models.CharField(max_length=20)
    Tb=models.CharField(max_length=20)
    Chest = models.CharField(max_length=20)
    Stroke = models.CharField(max_length=20)
    Fever = models.CharField(max_length=20)
    Attack = models.CharField(max_length=20)
    MVP=models.CharField(max_length=20,default='')
    Asthma = models.CharField(max_length=20)
    Pacemaker = models.CharField(max_length=20)
    Thyroid = models.CharField(max_length=20)

class Prescription(models.Model):
    docid=models.IntegerField()
    pid=models.IntegerField()
    Medicine=models.CharField(max_length=50)
    Dosage=models.CharField(max_length=20,default='')
    Nod=models.IntegerField()

class Article(models.Model):
    docid=models.IntegerField()
    Title=models.CharField(max_length=25)
    File=models.FileField(upload_to='file')
    Status=models.CharField(max_length=20)

class Answer(models.Model):
    qid=models.IntegerField()
    ans=models.CharField(max_length=200)