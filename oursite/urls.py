"""
oursite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

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

# Uncomment next two lines to enable admin:
#from django.contrib import admin
#from django.urls import path
from django.conf.urls import include,url
import login.views
import datatable.views
import chart.views
from django.views import static
from django.conf import settings 


urlpatterns = [
    # Uncomment the next line to enable the admin:
    #path('admin/', admin.site.urls)
    url(r'^login$',login.views.login,name='login'),
    url(r'^register$',login.views.register,name='register'),
    url(r'^changepsw$',login.views.changepsw,name='changepsw'),
    url(r'^logout$',login.views.logout,name='logout'),
    url(r'^adminlogin$',login.views.adminlogin,name='adminlogin'),
    url(r'^adminuser$',datatable.views.adminuser,name='adminuser'),
    url(r'^datatable$',datatable.views.datatable,name='datatable'),
    url(r'^datauser$',datatable.views.datauser,name='datauser'),
    url(r'^databack$',datatable.views.databack,name='databack'),
    url(r'^datainput$',datatable.views.datainput,name='datainput'),
    url(r'^dataalert$',datatable.views.dataalert,name='dataalert'),
    url(r'^chart_mymap$',chart.views.chart_mymap,name='chart_mymap'),
    url(r'^$',chart.views.chart_mymap,name='index'),
    url(r'^myMap$',chart.views.myMap,name='myMap'),
    url(r'^chart_mychart1$',chart.views.chart_mychart1,name='chart_mychart1'),
    url(r'^mychart1$',chart.views.mychart1,name='mychart1'),
    url(r'^chart_mychart2$',chart.views.chart_mychart2,name='chart_mychart2'),
    url(r'^mychart2$',chart.views.mychart2,name='mychart2'),
    url(r'^chart_mychart3$',chart.views.chart_mychart3,name='chart_mychart3'),
    url(r'^mychart3$',chart.views.mychart3,name='mychart3'),
    url(r'^static/(?P<path>.*)', static.serve,
      {'document_root': settings.STATIC_ROOT}, name='static'),
]

