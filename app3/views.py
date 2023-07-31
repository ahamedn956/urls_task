from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def dhoni(request):
    return render(request,'dhoni.html')
def virat(request):
    return render(request,'virat.html')
def cricket(request):
    return HttpResponse('<h2><i>This two are my favourite cricket players!!!!!')