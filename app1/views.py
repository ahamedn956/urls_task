from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def naruto(request):
    return render(request,'naruto.html')
def sasuke(request):
    return render(request,'sasuke.html')
def sakura(request):
    return HttpResponse('<h1><i>A SMILE IS THE EASIEST WAY OUT OF A DIFFICULT SITUATION.</i></h1>')