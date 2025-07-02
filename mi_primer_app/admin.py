from django.contrib import admin

# Register your models here.
from .models import Familiar, Curso, Estudiante

register_models = [Familiar, Curso, Estudiante]

admin.site.register(register_models)
