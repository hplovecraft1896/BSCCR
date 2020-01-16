"""BSCCR2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from Sentencias.views import SentenciaList,home,CuentadanteList,SentenciaDetalle,CuentadanteDetail,pdf_download

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('sentencias/', SentenciaList.as_view(), name='sentencias'),
    path('cuentadantes/', CuentadanteList.as_view(), name='cuentadantes'),
    path('sentencia/<int:pk>', SentenciaDetalle.as_view(), name='sentencia_detail'),
    path('cuentadante/<int:pk>', CuentadanteDetail.as_view(), name='cuentadante_detail'),
    path('pdfs/<filename>', pdf_download,name='pdf_download'),
]

#urlpatterns += [
#        static(settings.MEDIA_URL, document_root=settings.MEDIA_URL),
#        static(settings.STATIC_URL, document_root=settings.STATIC_URL),
#]


admin.site.site_header = "Panel de Administracion"
admin.site.site_title = "BSCCR Panel de Administracion"
admin.site.index_title = "Bienvenido Al Panel de Administracion de BSCCR"

