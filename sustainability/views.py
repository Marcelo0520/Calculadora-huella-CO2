from django.shortcuts import render
import requests
# Create your views here.

def home(request):
    return render(request,'inicio.html')

def nosotros(request):
    return render(request,'nosotros.html')


def calcular_huella_carbono(tiempo_uso, calidad, ancho_banda, tipo_servicio):
    response = requests.get("https://api.carboncloud.com/calculate", params={
        "service": tipo_servicio,
        "duration": tiempo_uso,
        "quality": calidad,
        "bandwidth": ancho_banda
    })
    return response.json()["carbon_footprint"]