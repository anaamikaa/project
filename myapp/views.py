from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html')

def homepg(request):
    return render(request, 'file.html')
# Create your views here.
