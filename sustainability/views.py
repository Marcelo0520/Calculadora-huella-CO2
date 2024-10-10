from django.shortcuts import render
import requests

def home(request):
    return render(request,'inicio.html')

def nosotros(request):
    return render(request,'nosotros.html')

def loginn(request):
    return render(request,'login.html')

def registro(request):
    return render(request,'registro.html')

def calcular_huella_carbono(tiempo_uso, calidad, ancho_banda, tipo_servicio):
    response = requests.get("https://api.carboncloud.com/calculate", params={
        "service": tipo_servicio,
        "duration": tiempo_uso,
        "quality": calidad,
        "bandwidth": ancho_banda
    })
    return response.json()["carbon_footprint"]