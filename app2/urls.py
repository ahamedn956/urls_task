from django.urls import path
from app2.views import *

app_name = 'django'

urlpatterns =[
    path('demo1/',demo1,name='demo1'),
    path('demo2/',demo2,name='demo2'),
    path('demo3/',demo3,name='demo3'),
]
