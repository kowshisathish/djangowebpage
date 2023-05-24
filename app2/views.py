from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def project2(request):
    return HttpResponse("django project")

def data2(request):
    return render(request,"data2.html")

