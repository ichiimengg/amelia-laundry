from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')),   # semua URL utama diarahkan ke app main
    path('admin/', admin.site.urls),
]
