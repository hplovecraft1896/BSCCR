from django.contrib import admin
from .models import Sentencia, Cuentadante,Reparo

# Register your models here.

class ReparoInline(admin.StackedInline):
    model = Reparo
    filter_horizontal = ('cuentadantes',)
    extra=0




class SentenciaAdmin(admin.ModelAdmin):
    list_display = ('numero','institucion','resolucion','camara','instancia',
                  'fecha_recepcion','fecha_resolucion',
                  'pdf',)
    search_fields=('numero','camara','instancia',)
    ordering=('fecha_recepcion','fecha_resolucion','camara','instancia',)
    inlines = [ReparoInline]


admin.site.register(Sentencia, SentenciaAdmin)

class CuentadanteAdmin(admin.ModelAdmin):
    list_display = ('nombre','institucion','cargo')

admin.site.register(Cuentadante, CuentadanteAdmin)

class ReparoAdmin(admin.ModelAdmin):
    list_display = ('numero_de_reparo','sentencia',)
    filter_horizontal = ('cuentadantes',)

#admin.site.register(Reparo, ReparoAdmin)
