
from django.contrib import admin
from django.urls import path
import helloworld.views





urlpatterns = [
    path('admin/', admin.site.urls),
    path('',helloworld.views.index, name='index')

]
