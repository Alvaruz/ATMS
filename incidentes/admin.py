from django.contrib import admin
from incidentes.models import *





@admin.register(Equipos) # nombre, descripcion
class EquipoRegister(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')

    # def get_categoria(self, obj):
    # 	return obj.categoria.descripcion
    # # get_categoria.admin.order_field = 'nombre'


@admin.register(Stock) # nombre, buenos, dañados
class StockRegister(admin.ModelAdmin):
    list_display = ('nombre', 'buenos',)


@admin.register(Grupo) # nombre, descripcion
class GrupoRegister(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')


@admin.register(Usuario) # nombre, apellido, grupo
class UsuarioRegister(admin.ModelAdmin):
    list_display = ('nombre', 'apellido')


@admin.register(Categoria) # nombre, descripcion, relevancia
class CategoriaRegister(admin.ModelAdmin):
    list_display = ('nombre', 'relevancia')


@admin.register(Estado) # nombre, descripcion
class EstadoRegister(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')


@admin.register(Ticket) # categoria, nombre, usuario, grupo_destino, detalle, equipo, fecha, estado
class TicketRegister(admin.ModelAdmin):
    list_display = ('categoria', 'ubicacion', 'grupo_destino', 'fecha', 'estado')



