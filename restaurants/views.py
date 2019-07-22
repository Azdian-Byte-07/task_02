from django.shortcuts import render

# Create your views here.

def first(req):
    context = {'msg': 'Hello World!'}
    return render(req, 'first.html', context)
