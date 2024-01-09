from django.contrib import admin
from django.urls import path
from cadastro_estudante import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('estudantes/', views.estudantes, name="lista_estudantes")
]
