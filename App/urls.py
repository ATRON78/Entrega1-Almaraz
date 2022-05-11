from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('padres/', padres, name='padres'),
    path('madres/', madres, name='madres'),
    path('hermanos/', hermanos, name='hermanos'),
    path('buscar/', buscar, name='buscar'),
]