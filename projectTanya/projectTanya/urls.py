from django.contrib import admin
from django.urls import path, include
from nii import views

urlpatterns = [
    path('', views.index),
    path('nii/', include('nii.urls')),
    path('admin/', admin.site.urls),
]
