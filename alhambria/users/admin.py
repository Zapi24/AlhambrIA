from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario


class UsuarioAdmin(UserAdmin):

    #Definimos que campos vamos a ver en la página de admin de DJango
    list_display = ('email', 'nombre', 'apellidos', 'puesto', 'is_staff') 

    #Eliminamos el username de los filtros y del ordenamiento
    ordering = ('email',)
    search_fields = ('email', 'nombre', 'apellidos')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Información Personal', {'fields': ('nombre', 'apellidos', 'telefono', 'puesto', 'foto_perfil')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nombre', 'apellidos', 'password'),
        }),
    )


# Register your models here.
admin.site.register(Usuario, UsuarioAdmin)

