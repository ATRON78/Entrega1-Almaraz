from django.contrib import admin
from .models import Padre, Madre, Hermano
# Register your models here.

admin.site.register(Padre)
admin.site.register(Madre)
admin.site.register(Hermano)