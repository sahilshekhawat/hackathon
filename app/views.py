# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from google.appengine.api import users


def index(request):
    user = users.get_current_user()
    if user:
        greetings = ('welcome, %s!' % (user.nickname()))
        href = users.create_logout_url('/')
    else:
        greetings = ('You must LOGIN first!')
        href = users.create_login_url('/')

    return render(request, 'index.html', {'title' : 'hackathon' , 'greetings' : greetings , 'href' : href})
