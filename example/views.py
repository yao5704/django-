from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def right(request):
    return render(request,'right.html')

def error(request):
    return render(request,'error.html')
# Create your views here.
