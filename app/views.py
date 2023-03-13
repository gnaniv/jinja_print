from django.shortcuts import render

# Create your views here.

def first(request):
    d={'name':'ANJU'}
    return render(request,'jinja.html',context=d)
