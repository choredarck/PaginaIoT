from django.contrib.auth import get_user_model
from django.shortcuts import render, HttpResponse
from django.views.generic import View
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response

User= get_user_model()

import datetime
from django.template import	 Template, Context

def saludo(request):#primera
    nombre="Hora Actual"
    apellido= datetime.datetime.now() 
    doc_externo= open("C:/Users/Chore-Darc/Desktop/CUCEI/Projects Django/pruebita/pruebita/templates/charts.html")        
    plt= Template(doc_externo.read())
    doc_externo.close() 
    ctx= Context({"nombre_persona": nombre, "apellido_persona": apellido}) #corchetes para indidacr que vamos a recibir un valor
    documento= plt.render(ctx) 
    return HttpResponse(documento)


def dameFecha(request):
    fecha_actual= datetime.datetime.now()
    documento="""<htmnl>
    <body>
    <h2>
    Fecha y hora actuales %s
    </h2>
    </body>
    </htmnl>""" % fecha_actual
    return HttpResponse(documento)


def calculaEdad(request, edad, agno):
    #edadActual= 24
    periodo= agno - 2020 
    edadFutura= edad+periodo
    documento="""<htmnl>
    <body>
    <h2>
    En el año %s tendras %s años
    </h2>
    </body>
    </htmnl>""" % (agno, edadFutura)
    return HttpResponse(documento)


class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'Index.html', {})

def get_data(request, *args, **kwargs):
    data= {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data)


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs_count= User.objects.all().count()
        labels = ["User", "Blue", "Yellow", "Green", "Purple", "Orange"]
        default_items= [qs_count, 25, 32, 32, 12, 7]
        data= {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)