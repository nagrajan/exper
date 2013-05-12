# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from forms import MyUserCreationForm

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def logout(request):
    username = request.user.username
    auth.logout(request)
    return render_to_response('logout.html', {'full_name': username})
    pass

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
    return render_to_response('loggedin.html', {'full_name':request.user.username})

def invalid_login(request):
    return render_to_response('invalid.html', {'username':request.user.username})

def register_user(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')

    args = {}
    args.update(csrf(request))
    args['form'] = MyUserCreationForm()
    return render_to_response('register.html', args)

def register_success(request):
    return render_to_response('register_success.html')



