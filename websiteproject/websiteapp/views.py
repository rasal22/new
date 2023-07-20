from django.shortcuts import render
from . models import place
from . models import team
# Create your views here.
def demo(request):
    obj = place.objects.all()
    object = team.objects.all()
    return render(request, "index.html", {'result': obj,'resultt':object})
# def demo1(request):
#      obj=team.objects.all()
#      return render(request,"index.html",{'result':obj})

