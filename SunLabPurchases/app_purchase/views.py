from django.shortcuts import render, HttpResponse

# Create your views here.
def hoome(request):
    return HttpResponse("Hello, World!")
    