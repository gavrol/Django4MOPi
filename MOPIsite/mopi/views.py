from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def home(request,template_name):

    return render(request,template_name)
