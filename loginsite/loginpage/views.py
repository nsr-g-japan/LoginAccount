from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from microsoft_authentication.auth.auth_decorators import microsoft_login_required
from microsoft_authentication.auth.auth_utils import get_token_from_code, get_user



def homepage(request):
    return HttpResponse("<h1>HI Nisar Basha </h1>")


