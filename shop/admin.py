from email.charset import add_alias
from django.contrib import admin
from .models import Category, Product, Commande

#Changer le du titre de la page d'administration
admin.site.site_header = "Kevine-Shop Administration"

#Changer le titre de la fenetre
admin.site.site_title = "Kevine-Shop"
admin.site.index_title = "Manager"

# Relier les models a l'interface administrateur

class AdminCategorie(admin.ModelAdmin):
    list_display = ('name', 'date_added',)
    

class AdminProduct(admin.ModelAdmin):
    list_display = ('title','price', 'category', 'date_added')
    search_fields = ('title',)
    list_editable = ('price',)
    
    
class AdminCommande(admin.ModelAdmin):
    list_display = ('items', 'nom', 'email', 'address', 'ville', 'pays', 'total', 'zipcode', 'date_commande',)
  
admin.site.register(Category, AdminCategorie)
admin.site.register(Product, AdminProduct)
admin.site.register(Commande, AdminCommande)

