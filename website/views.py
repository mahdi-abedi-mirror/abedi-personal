from django.shortcuts import render

def index (requset):
    return render (requset ,"website/index.html")