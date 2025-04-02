from django.shortcuts import render
from django.http import HttpResponse

def showdetail(request, show_id):
    return HttpResponse("You found show %s" % show_id)