#encoding: utf-8

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def log_me_in(request, *args):
    if request.method == "GET":
        return render_to_response("login.html", None, context_instance=RequestContext(request))
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/")
        else:
            return HttpResponse('''<SCRIPT LANGUAGE="JavaScript" TYPE="text/javascript">alert ("Login/Senha inválido."); window.location.href="/login/";</SCRIPT>''')
 
def log_me_out(request, *args):
    logout(request)
    return render_to_response("index.html")

def index(request, *args):
    if request.user.is_authenticated():
        return render_to_response("index.html", {'logged' : True, 'username': request.user})
    else:
        return render_to_response("index.html", {'logged' : False})

def watch(request, *args):
    return render_to_response("watch.html")

@login_required
def upload(request, *args):
    return render_to_response("upload.html")

def subscribe(request, *args):
    if request.method == "GET":
        return render_to_response("subscribe.html", None, context_instance=RequestContext(request))
    elif request.method == "POST":
        _name = request.POST['name'].strip()
        _email = request.POST['email'].strip()
        _username = request.POST['username'].strip()
        _password = request.POST['password']
        try:
            user = User.objects.get(username=_username)
            return HttpResponse('''<SCRIPT LANGUAGE="JavaScript" TYPE="text/javascript">alert ("Usuário já existe. 
                                Escolha outro login."); window.location.href="/subscribe/";</SCRIPT>''')
        except User.DoesNotExist:
            user = User.objects.create_user(_username, _email, _password)
            user.first_name = _name
            user.save()
            auth = authenticate(username=_username, password=_password)
            if auth is not None:
                login(request, auth)
                return HttpResponseRedirect("/")
            else:
                return HttpResponse("Deu águia")



