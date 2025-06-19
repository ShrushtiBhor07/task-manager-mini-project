from django.shortcuts import render,redirect
from .models import Task

def index(request):
    if request.method=="POST":
        title=request.POST.get('title')
        if title:
            Task.objects.create(title=title)
            return redirect('/')
    tasks=Task.objects.all()
    return render(request, template_name='index.html',context={'tasks':tasks})

# Create your views here.
