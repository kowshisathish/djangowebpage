from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def project(request):
    return HttpResponse('<marquee><h1>django is a framework</h1></marquee>')

def data(request):
    return render(request,"data.html")
