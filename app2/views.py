from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def demo1(request):
    return render(request,'demo1.html')
def demo2(request):
    return render(request,'demo2.html')
def demo3(request):
    return HttpResponse('<h2>JS is a programming language that is one of the core technologies of the World Wide Web</h2>')