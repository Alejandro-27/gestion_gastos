from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from core import views

urlpatterns = [
    path("", views.home, name="home"),
    path("admin/", admin.site.urls),
    path("registro/", views.registro, name="registro"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="usuarios/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    
    path("gastos/registrar/", views.registrar_gastos, name="registrar_gastos"),
    path("gastos/editar/<int:gasto_id>/", views.editar_gastos, name="editar_gastos"),
    path("gastos/listar/", views.listar_gastos, name="listar_gastos"),
    path("gastos/eliminar/<int:gasto_id>/", views.eliminar_gastos, name="eliminar_gastos"),
]