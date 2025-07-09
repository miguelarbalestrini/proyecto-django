from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .models import Familiar, Curso, Estudiante, Auto

from .forms import CursoForm, EstudianteForm, AutoForm

# Create your views here.
from django.http import HttpResponse

# view de inicio


def inicio(request):
    return render(request, 'mi_primer_app/inicio.html')


def saludo(request):
    return HttpResponse("¡Hola, mundo!")


def saludo_con_template(request):
    return render(request, 'mi_primer_app/saludo.html')


def crear_familiar(request, nombre):
    if nombre is not None:
        # Creamos un nuevo objeto Familiar
        nuevo_familiar = Familiar(
            nombre=nombre,
            apellido="ApellidoEjemplo",
            edad=30,
            fecha_nacimiento="1993-01-01",
            parentesco="Primo"
        )
        nuevo_familiar.save()
    return render(request, "mi_primer_app/crear_familiar.html", {"nombre": nombre})


def crear_curso(request):

    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            # Procesar el formulario y guardar el curso
            nuevo_curso = Curso(
                nombre=form.cleaned_data['nombre'],
                descripcion=form.cleaned_data['descripcion'],
                duracion_semanas=form.cleaned_data['duracion_semanas'],
                fecha_inicio=form.cleaned_data['fecha_inicio'],
                activo=form.cleaned_data['activo']
            )
            nuevo_curso.save()
            return redirect('cursos')
    else:
        form = CursoForm()
        return render(request, 'mi_primer_app/crear_curso.html', {'form': form})


def crear_estudiante(request):

    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            # Procesar el formulario y guardar el curso
            nuevo_curso = Estudiante(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                email=form.cleaned_data['email'],
                edad=form.cleaned_data['edad'],
                fecha_inscripcion=form.cleaned_data['fecha_inscripcion']
            )
            nuevo_curso.save()
            return redirect('inicio')
    else:
        form = EstudianteForm()
        return render(request, 'mi_primer_app/crear_estudiante.html', {'form': form})


def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'mi_primer_app/cursos.html', {'cursos': cursos})


def buscar_cursos(request):
    if request.method == 'GET':
        nombre = request.GET.get('nombre', '')
        cursos = Curso.objects.filter(nombre__icontains=nombre)
        return render(request, 'mi_primer_app/cursos.html', {'cursos': cursos, 'nombre': nombre})


class AutoListView(ListView):
    model = Auto
    template_name = 'mi_primer_app/listar_autos.html'
    context_object_name = 'autos'


class AutoCreateView(CreateView):
    model = Auto
    form_class = AutoForm
    template_name = 'mi_primer_app/crear_auto.html'
    success_url = reverse_lazy('listar-autos')


class AutoDetailView(DetailView):
    model = Auto
    template_name = 'mi_primer_app/detalle_auto.html'
    context_object_name = 'auto'


class AutoUpdateView(UpdateView):
    model = Auto
    form_class = AutoForm
    template_name = 'mi_primer_app/crear_auto.html'
    success_url = reverse_lazy('listar-autos')


class AutoDeleteView(DeleteView):
    model = Auto
    template_name = 'mi_primer_app/eliminar_auto.html'
    success_url = reverse_lazy('listar-autos')
