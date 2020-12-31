from django.contrib import admin
from django.urls import path, include
from school import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

# you could register other apis too
router.register('studentapi', views.StudentModelViewSet, basename="student")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),	
]
