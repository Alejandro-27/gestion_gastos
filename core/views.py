from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import RegistroForm
from .models import Gastos


def home(request):
    return render(request, "base/home.html")


def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegistroForm()
    return render(request, "usuarios/registro.html", {"form": form})


def registrar_gastos(request):
    if request.method == "POST":
        descripcion = request.POST.get("descripcion")
        monto = request.POST.get("monto")

        if descripcion and monto:
            nuevo_gasto = Gastos(descripcion=descripcion, monto=monto)
            if request.user.is_authenticated:
                nuevo_gasto.usuario = request.user

            nuevo_gasto.save()
            messages.success(request, "¡El gasto se ha registrado correctamente!")
            return redirect("listar_gastos")

    gastos_list = Gastos.objects.all().order_by("-fecha")
    return render(request, "gastos/registrar_gastos.html", {"gastos": gastos_list})


def editar_gastos(request, gasto_id):
    gasto = get_object_or_404(Gastos, id=gasto_id)
    if request.method == "POST":
        gasto.descripcion = request.POST.get("descripcion")
        gasto.monto = request.POST.get("monto")
        gasto.save()
        messages.success(request, "¡El gasto se ha actualizado correctamente!")
        return redirect("listar_gastos")
    return render(request, "gastos/editar_gastos.html", {"gasto": gasto})


def listar_gastos(request):
    gastos = Gastos.objects.all().order_by("-fecha")
    return render(request, "gastos/listar_gastos.html", {"gastos": gastos})


def eliminar_gastos(request, gasto_id):
    gasto = get_object_or_404(Gastos, id=gasto_id)
    gasto.delete()
    messages.success(request, "¡El gasto se ha eliminado correctamente!")
    return redirect("listar_gastos")
