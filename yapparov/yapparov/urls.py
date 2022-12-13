from type import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path("create", views.create),
    path("edit/<int:id>", views.edit),
    path("delete/<int:id>", views.delete),
]