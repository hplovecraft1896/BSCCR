from django import forms

from .models import Sentencia, Cuentadante

class SentenciaForm(forms.ModelForm):

    class Meta:
        model = Sentencia
        fields = ('numero','resumen','resolucion','camara',
                  'fecha_recepcion','fecha_resolucion',
                  'pdf',)
