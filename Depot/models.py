from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.conf import settings
# Create your models here.
 

class Client(AbstractUser):
    name=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True,default="")
    adresse=models.CharField(max_length=200,null=True,default="")
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    

    def __str__(self):
        return self.name

class Medicament(models.Model):
     code=models.AutoField(primary_key=True)
     name=models.CharField(max_length=200,null=True,default="")
     prix = models.FloatField(null=True)
     Description=models.TextField(max_length=200,null=True)

     def __str__(self):
        return self.name



class Commande(models.Model):
    STATUS=(
        ('pending','pending'),
        ('Out for delivrey','Out for delivrey'),
        ('delivrey','delivrey')
        )
    id_commande = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    medicament= models.ForeignKey(Medicament, on_delete=models.CASCADE)
    status=models.CharField(max_length=200,null=True,choices=STATUS,default="")
    location =models.CharField(max_length=200,null=True,default="")
    date_created=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return str(self.id_commande) +' de medicament : '+str(self.medicament)+'par:  '+ str(self.client.name)

