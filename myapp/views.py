from django.shortcuts import render

# Create your views here.

def info(request):
    data={'name':'azhar','age':22,'gender':'Male','marks':[100,200]}
    return render(request,'info.html',data)

