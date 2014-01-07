# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from google.appengine.api import users
from models import date
from models import account

def index(request):
    user = account()
    user_function =users.get_current_user()
    user.email = user_function.email()
    user.user_id = int(user_function.user_id())
    user.username = user_function.nickname()
    #user_key = user.put()
    if user:
        greetings = ('welcome, %s!' % (user.username))
        link = "Logout"
        href = users.create_logout_url('/')
    else:
        greetings = ('You must LOGIN first!')
        href = users.create_login_url('/')
        link = "Login"

    return render(request, 'index.html', {'title' : 'hackathon' , 'greetings' : greetings , 'href' : href , 'link' : link})
