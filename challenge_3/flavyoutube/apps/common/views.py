#encoding: utf-8

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django import forms

class UploadMovieForm(forms.Form):
    name = forms.CharField(max_length=100, label="Nome")
    description = forms.CharField(label="Descrição", widget=forms.Textarea)
    video = forms.FileField()
    rotate = forms.BooleanField(label="Rotacionar Video", required=False)

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
    if request.method == 'GET':
        form = UploadMovieForm()
        return render_to_response("upload.html", {'logged' : True, 'username': request.user, 'form': form}, context_instance=RequestContext(request))

    elif request.method == 'POST':
        form = UploadMovieForm(request.POST, request.FILES)
        if form.is_valid():
            if handle_video_upload(request.FILES['video']):
                return render_to_response("upload.html", {'logged' : True, 'upload_success':True, 
                        'username': request.user, 'form': form}, context_instance=RequestContext(request))
        
        return render_to_response("upload.html", {'logged' : True, 'upload_fail':True, 
                'username': request.user, 'form': form}, context_instance=RequestContext(request))
                

def handle_video_upload(movie):
    for chunk in movie.chunks():
        print 'ok'
    return True

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
            login(request, auth)
            return HttpResponseRedirect("/")



