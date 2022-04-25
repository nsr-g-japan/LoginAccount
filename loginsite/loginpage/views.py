from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from microsoft_authentication.auth.auth_decorators import microsoft_login_required

from .auth_helper import *
from .graph_helper import *


@microsoft_login_required()
def home(request):
    return HttpResponse("Logged in")


# If pages need to be restricted to certain groups of users.


def homepage(request):
    return render(request, 'homepage.html', {})


def landingpage(request):
    # Make the token request
    result = get_token_from_code(request)  # Get the user's profile from graph_helper.py script
    user = get_user(result['access_token'])  # Store user from auth_helper.py script
    store_user(request, user)

    username = user['displayName']
    password = user['surname']
    email = user['mail']
    print(username, password, email)

    return render(request, 'landingpage.html', {})
