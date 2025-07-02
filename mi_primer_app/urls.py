from django.urls import path

from .views import saludo, saludo_con_template, crear_familiar, inicio, crear_curso, crear_estudiante, buscar_cursos, cursos

urlpatterns = [
    path('', inicio, name='inicio'),
    path('hola-mundo/', saludo),
    path('hola-mundo-template/', saludo_con_template),
    path('crear-familiar/<str:nombre>/', crear_familiar),
    path('crear-curso/', crear_curso, name='crear-curso'),
    path('crear-estudiante/', crear_estudiante, name='crear-estudiante'),
    path('cursos/', cursos, name='cursos'),
    path('cursos/buscar', buscar_cursos, name='buscar-cursos'),
]
