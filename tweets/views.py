from django.shortcuts import render

def home_view(request,*args,**kwargs):
   return HttpResponse('<h1> hello world </h1>')
