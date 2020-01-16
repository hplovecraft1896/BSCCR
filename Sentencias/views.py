import os

from django.shortcuts import render
from django.views.generic import DetailView,View,CreateView,ListView,DeleteView
from django.urls import reverse
from wsgiref.util import FileWrapper
from django.http import HttpResponse,FileResponse,HttpResponseNotFound

from .models import Cuentadante, Sentencia,Reparo
from .forms import SentenciaForm


def home(request):
    return render(request,"home.html",{})


#Sentencia
class SentenciaDetalle(DetailView):
    model = Sentencia
    context_object_name = 'sentencia'
    template_name='Sentencias/sentencia_detalle.html'

    def get_context_data(self, **kwargs):
        context = super(SentenciaDetalle, self).get_context_data(**kwargs)
        context['reparos'] = Reparo.objects.filter(sentencia=self.object)
        context['filename'] = os.path.basename(self.object.pdf.name)
        return context


class SentenciaCreateView(CreateView):
    model = Sentencia
    form_class = SentenciaForm
    template_name = "Sentencias/sentencia_crear.html"


class SentenciaList(ListView):
    model = Sentencia
    context_object_name = 'sentencias'
    template_name='Sentencias/sentencia_lista.html'
    #paginate_by = 30

    def get_queryset(self):
        numero = self.request.GET.get('numero')

        if numero:
            sentencias = Sentencia.objects.filter(numero__icontains=numero)
            return sentencias
        return Sentencia.objects.all()


#Cuentadantes
class CuentadanteDetail(DetailView):
    model = Cuentadante
    template_name='Sentencias/cuentadante_detalle.html'
    context_object_name = 'cuentadante'

    def get_context_data(self, **kwargs):
        context = super(CuentadanteDetail, self).get_context_data(**kwargs)
        reparos = Reparo.objects.filter(cuentadantes__in=[self.object.id])
        sentencias = []
        for reparo in reparos:
            if reparo.sentencia.pk not in sentencias:
                sentencias.append(reparo.sentencia.pk)      
        context['reparos'] = reparos
        context['sentencias'] = len(sentencias)
        return context
    

class CuentadanteList(ListView):
    model = Cuentadante
    context_object_name = 'cuentadantes'
    template_name ='Sentencias/cuentadante_lista.html'
    #paginate_by = 30

    def get_queryset(self):
        nombre = self.request.GET.get('nombre')

        if nombre:
            cuentadantes = Cuentadante.objects.filter(nombre__icontains=nombre)
            return cuentadantes
        return Cuentadante.objects.all()

#pdf
def pdf_download(request, filename):
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(base,"PDF_sentencias",filename)
    print(path)
    try:    
        file_data = open(path, 'rb')
        # sending response 
        response = FileResponse(file_data, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="' + filename + '"'

    except IOError:
        # handle file not exist case here
        response = HttpResponseNotFound('<h1>File not exist</h1>')

    return response


