from django.contrib import admin
from django.urls import path
from sustainability import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="inicio"),
    path('/nosotros',views.nosotros,name="nosotros"),
]
