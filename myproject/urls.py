"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from myapp.views import run_scripts, index ,upload_images


urlpatterns = [
    path('', include('myapp.urls')),
    path("admin/", admin.site.urls),

#     path('run-scripts/', run_scripts, name='run_scripts'),
#     path('', index, name='index'),
#     path('upload-images/', upload_images, name='upload_images'),
 ]








