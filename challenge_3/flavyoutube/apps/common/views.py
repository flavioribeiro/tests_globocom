from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

def login(request, *args):
    return render_to_response("login.html")

def logout(request, *args):
    return HttpResponseRedirect("/")

def index(request, *args):
    return render_to_response("index.html")

def watch(request, *args):
    return render_to_response("watch.html")

def upload(request, *args):
    return render_to_response("upload.html")
