
from django.contrib import admin
from django.urls import path

from .views import *
urlpatterns = [
    path('calcs/', listtodo.as_view()),
    # path('read/', read.as_view())

]
   