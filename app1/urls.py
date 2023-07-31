from django.urls import path
from app1.views import *

app_name ='anime'

urlpatterns =[
    path('naruto/',naruto,name='naruto'),
    path('sasuke/',sasuke,name='sasuke'),
    path('sakura/',sakura,name='sakura'),
]