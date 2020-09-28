from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from csv_file.views import csv_upload,external

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('external/', external),
    path('upload-csv/', csv_upload, name="csv_upload"),
]