from django.http import HttpResponse
from django.shortcuts import render
from .  models import Place1
from . models import Team1
# Create your views here.
def demo(request):
    obj=Place1.objects.all()
    obj1=Team1.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})
