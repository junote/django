from django.shortcuts import render

# Create your views here.

def bootstrap(request):
    return render(request,"bootstrap.html")

def bs2(request):
    return render(request,"bs2.html")
