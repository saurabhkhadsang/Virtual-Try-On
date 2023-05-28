from django.urls import path
from myapp.views import index,upload_images,run_scripts

urlpatterns = [
    path('', index, name='index'),
    path('upload-images/', upload_images, name='upload_images'),
    path('run_scripts', run_scripts, name='run_scripts'),

]


