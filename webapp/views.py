from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    context_dict = {'pages': "hello."}
    return render(request, 'index.html', context_dict)
