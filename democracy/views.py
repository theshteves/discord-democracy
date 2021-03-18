from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Under Construction')

def other(request, route):
    print(request)
    context = {'msg': 'Hello World!'}
    return render(request, 'other.html', context)
