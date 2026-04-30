from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .models import Gastos
from .forms import RegistroForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, 'base/home.html')

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})


@login_required
def registrar_gastos(request):
    if request.method == 'POST':
        descripcion = request.POST.get('descripcion')
        monto = request.POST.get('monto')
        if descripcion and monto:
            Gastos.objects.create(
                descripcion=descripcion, 
                monto=monto
            )
            messages.success(request, '¡El gasto se ha registrado correctamente!')
            return redirect('listar_gastos')
    
    gastos_list = Gastos.objects.all()
    return render(request, 'gastos/registrar_gastos.html', {'gastos': gastos_list})


@login_required
def editar_gastos(request, gasto_id):
    gasto = get_object_or_404(Gastos, id=gasto_id)
    if request.method == 'POST':
        gasto.descripcion = request.POST.get('descripcion')
        gasto.monto = request.POST.get('monto')
        gasto.save()
        messages.success(request, '¡El gasto se ha actualizado correctamente!')
        return redirect('listar_gastos')
    return render(request, 'gastos/editar_gastos.html', {'gasto': gasto})


@login_required
def listar_gastos(request):
    gastos = Gastos.objects.all().order_by('-fecha')
    return render(request, 'gastos/listar_gastos.html', {'gastos': gastos})

@login_required
def eliminar_gastos(request, gasto_id):
    gasto = get_object_or_404(Gastos, id=gasto_id)
    gasto.delete()
    messages.success(request, '¡El gasto se ha eliminado correctamente!')
    return redirect('listar_gastos')
