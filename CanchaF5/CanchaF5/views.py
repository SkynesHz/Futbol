from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
#from django.template.loader import get_template
from django.shortcuts import render

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


def saludo(request):
    p1=Persona("Profesor Juan", "Díaz")

    #nombre = "Juan"

    #apellido = "Díaz"

    temasCurso = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]

    ahora = datetime.datetime.now()

    #doc_externo = open("C:/Users/maria/Desktop/Proyecto1/Proyecto1/Proyecto1/templates/plantilla1.html")

    #plt = Template(doc_externo.read())

    #doc_externo.close()

    ## doc_externo = loader.get_template('plantilla1.html')

    #ctx = Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "tiempo": ahora, "temas": temasCurso })

    #documento = doc_externo.render({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "tiempo": ahora, "temas": temasCurso })

    #return HttpResponse(documento)
    return render(request, "plantilla1.html", {"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "tiempo": ahora, "temas": temasCurso })


def despedida(request):
    return HttpResponse("Hasta luego Django")


def dameFecha(request):
    fecha_actual = datetime.datetime.now()

    documento="""<html>
    <body>
    <h3>Fecha y hora actuales %s</h3>
    </body>
    </html>""" %fecha_actual

    return HttpResponse(documento)

def calculaEdad(request, edad, agno):
    periodo=agno-2021
    edadFutura=edad+periodo
    documento="<html><body><h2>En el año %s tendrás %s años</body></html>" %(agno,edadFutura)

    return HttpResponse(documento)

def CursoJava(request):
    fecha_actual = datetime.datetime.now()

    return render(request, "hija1.html", {"dameFecha": fecha_actual})

def home(request):
    return render(request, "principal.html")

def ubicacion(request):
    return render(request, "ubicacion.html")