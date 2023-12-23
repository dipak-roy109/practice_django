from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Person)
class Personadmin(admin.ModelAdmin):
    list_display = ['id','name','age']

@admin.register(Nid)
class Nidadmin(admin.ModelAdmin):
    list_display = ['person','id_no']

@admin.register(Cetegory)
class Cetegoryadmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(Product)
class Productadmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'cetegory']

@admin.register(Group)
class Groupadmin(admin.ModelAdmin):
    list_display = ['id', 'name']

    
