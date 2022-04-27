from django.contrib import admin
from django.urls import path, include
from personal.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home),
    path('', include('personal.urls'))
]
