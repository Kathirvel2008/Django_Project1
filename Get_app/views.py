from django.shortcuts import render
from Get_app.models import Login
# Create your views here.
def display(request):
    demo = Login.objects.all()
    return render(request,'display.html',context={'data':demo})
