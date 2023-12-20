from django.contrib import admin
from django.contrib import admin
from usuarios.models import Datosusuario
from usuarios.forms import CreateUserForm
from django.contrib.auth.models import User

# Register your models here.

"""

admin.site.register(Datosusuario)

class CustomUserAdmin(User):
    add_form = CreateUserForm
    model = User
    list_display = [
        "usuario",
        "imagen", 
        "nombre",               
        "apellido",             
        "fecha_nacimiento",    
        "pais",                 
        "provincia",            
        "ciudad",               
        "domicilio",            
        "codigo_postal",       
        "telefono",             
        "celular",            
        "documento",            
        "cuit",                 
    ]
    
admin.site.register(CustomUserAdmin)
"""
