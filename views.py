from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'Assignment\home.html')

def Contact_Us(request):
    return render(request ,'Assignment\contact.html')
