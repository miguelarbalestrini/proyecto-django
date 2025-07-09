from django.urls import path

from .views import (saludo, saludo_con_template, crear_familiar,
                    inicio, crear_curso, crear_estudiante, buscar_cursos, cursos,
                    AutoCreateView, AutoListView, AutoDeleteView, AutoDetailView, AutoUpdateView)

urlpatterns = [
    path('', inicio, name='inicio'),
    path('hola-mundo/', saludo),
    path('hola-mundo-template/', saludo_con_template),
    path('crear-familiar/<str:nombre>/', crear_familiar),
    path('crear-curso/', crear_curso, name='crear-curso'),
    path('crear-estudiante/', crear_estudiante, name='crear-estudiante'),
    path('cursos/', cursos, name='cursos'),
    path('cursos/buscar', buscar_cursos, name='buscar-cursos'),

    # urls con vistas basadas en clase
    path('listar-autos/', AutoListView.as_view(), name='listar-autos'),
    path('crear-auto/', AutoCreateView.as_view(), name='crear-auto'),
    path('detalle-auto/<int:pk>', AutoDetailView.as_view(), name='detalle-auto'),
    path('editar/<int:pk>/', AutoUpdateView.as_view(), name='editar-auto'),
    path('eliminar/<int:pk>/', AutoDeleteView.as_view(), name='eliminar-auto'),

]
