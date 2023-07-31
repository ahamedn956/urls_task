from django.urls import path
from app3.views import *

app_name = 'cricket'

urlpatterns =[
    path('dhoni/',dhoni,name='dhoni'),
    path('virat/',virat,name='virat'),
    path('cricket/',cricket,name='cricket'),
]