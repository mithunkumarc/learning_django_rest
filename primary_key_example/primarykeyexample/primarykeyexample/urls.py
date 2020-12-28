from django.contrib import admin
from django.urls import path
from supermarket import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fruits/', views.fruitList),
    path('fruitcreate/', views.fruitCreate)
]
