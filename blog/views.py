from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def about(request):
    return HttpResponse('This is about page')

def home(request):
    return render(request, 'home.html', {'gret': 'hellpw!'})

