from django.db import models
from django.urls import reverse

# Create your models here.
class Cuentadante(models.Model):
    nombre = models.CharField(("Nombre"), max_length=200)
    salario = models.DecimalField(("Salario"), max_digits=8, decimal_places=2,blank=True,null=True)
    institucion = models.CharField(("Institucion"), max_length=200)
    cargo = models.CharField(("Cargo que desempeña"), max_length=200, blank=True,null=True)

    class Meta:
        verbose_name = 'Cuentadante'
        verbose_name_plural = 'Cuentadantes'

    def __str__(self):
        return '{} - {}'.format(self.nombre,self.institucion) # TODO

class Sentencia(models.Model):
    ResolucionChoices = [
        (True, 'Favorable'),
        (False, 'Desfavorable'),
        (None, 'Mixta')
    ]
    CamaraChoices = [
        (1,'Primera'),
        (2,'Segunda'),
        (3,'Tercera'),
        (4,'Cuarta'),
        (5,'Quinta'),
        (6,'Sexta'),
        (7,'Septima'),
    ]
    InstanciaChoices= [
        (1,'Primera'),
        (2,'Segunda'),
    ]
    numero = models.CharField(("Numero"), max_length=50,blank=True, null=True)
    instancia = models.IntegerField(("Instancia"),choices=InstanciaChoices)
    camara = models.IntegerField(("Camara"),blank=True, null=True,choices=CamaraChoices)
    institucion = models.CharField(("Institucion"), max_length=200,blank=True, null=True)
    fecha_resolucion = models.DateField(("Fecha de Resolucion"), auto_now=False, auto_now_add=False,blank=True, null=True)
    fecha_recepcion = models.DateField(("Fecha de Recepcion de Solicitud"), auto_now=False, auto_now_add=False,blank=True, null=True)
    resolucion = models.BooleanField(("Resolucion"),choices=ResolucionChoices,blank=True, null=True)
    resumen = models.TextField(("Resumen"),blank=True, null=True)
    pdf = models.FileField(("Archivo"), upload_to='PDF_sentencias/', max_length=100,blank=True, null=True)
    #agente_auxiliar = models.CharField(("Agente Auxiliar"), max_length=200,blank=True, null=True)

    class Meta:
        verbose_name = ("sentencia")
        verbose_name_plural = ("sentencias")
    
    def __str__(self):
        return self.numero

    def get_absolute_url(self):
        return reverse("sentencia_detail", kwargs={"pk": self.pk})


class Reparo(models.Model):
    """Model definition for Reparo."""
    titulo = models.CharField(max_length=200, blank=True, null=True)
    numero_de_reparo = models.CharField(("Numero De Reparo"), max_length=50)
    sentencia = models.ForeignKey('Sentencias.Sentencia', related_name='Sentencia', on_delete=models.CASCADE)
    cuentadantes = models.ManyToManyField('Sentencias.Cuentadante',related_name='Reparados', verbose_name=("Cuentadantes"))
    class Meta:
        """Meta definition for Reparo."""

        verbose_name = 'Reparo'
        verbose_name_plural = 'Reparos'

    def __str__(self):
        """Unicode representation of Reparo."""
        return 'Reparo: {} - Sentencia: {}'.format(self.numero_de_reparo,self.sentencia )
