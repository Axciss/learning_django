# from django.http import HttpResponse
from django.shortcuts import render

def hompage(request):
    # return HttpResponse("Hello world!")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("My about page")
    return render(request, 'about.html')