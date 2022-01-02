from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

def index(request):
    return HttpResponse('app02 response')


