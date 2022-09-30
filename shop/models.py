from email.mime import image
from turtle import title
from unicodedata import category, name
from django.db import models

# Creation de la tables de categorie dans la base de donner
class Category(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)
    
    #Classement des produits du nouveaux as l'encient
    class Meta:
        ordering = ['-date_added']
       
    # permet de donner le nom de la category dans l'interface administrateur 
    def __str__(self):
        return self.name
        

# Creation de la tables produit dans la base de donner
class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='Category', on_delete=models.CASCADE)
    image = models.CharField(max_length=6000)
    date_added = models.DateTimeField(auto_now=True)
    
    #Classement des produits du nouveaux as l'encient
    class Meta:
        ordering = ['-date_added']
        
    # permet de donner le nom de la category dans l'interface administrateur     
    def __str__(self):
        return self.title
    

class Commande(models.Model):
    items = models.CharField(max_length=300)
    total = models.CharField(max_length=200)
    nom = models.CharField(max_length=150)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    ville = models.CharField(max_length=200)
    pays = models.CharField(max_length=300)
    zipcode = models.CharField(max_length=300)
    date_commande = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_commande']
        
    def __str__(self):
        return self.nom