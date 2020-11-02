"""pruebita URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

#from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from pruebita import views
#from .views import saludo, dameFecha, calculaEdad, HomeView, get_data

from django.conf import settings
from django.conf.url.static import static

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('saludo/', views.saludo, name= "que-onda"),
    #path('fecha/', dameFecha), 
    #path('edades/<int:edad>/<int:agno>', calculaEdad),
    path('', views.HomeView.as_view(), name="home"),
    path('api/data/', views.get_data, name="api-data"),
    path('api/chart/data/', views.ChartData.as_view()),   
] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
