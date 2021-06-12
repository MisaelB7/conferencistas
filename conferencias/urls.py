from django.contrib import admin
from django.urls import path
from app_registro import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('participantes/',views.participantes, name="participantes"),
    path('participantes/<int:id>/eliminar/', views.eliminar_participante, name='eliminar_participante'),
    path('participantes/<int:id>/editar/', views.editar_participante, name='editar_participante'),
    path('conferencistas/',views.conferencistas, name="conferencistas"),
]
