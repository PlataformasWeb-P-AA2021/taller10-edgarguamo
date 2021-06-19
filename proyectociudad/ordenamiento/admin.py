from django.contrib import admin

from ordenamiento.models import Parroquia, Barrio
# Register your models here.
class ParroquiaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo')
    search_fields = ('nombre','tipo')

admin.site.register(Parroquia, ParroquiaAdmin)

class BarrioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'num_viviendas', 'num_parques', 'num_edificios',
            'parroquia')
    search_fields = ('nombre', 'parroquia')

admin.site.register(Barrio, BarrioAdmin)
