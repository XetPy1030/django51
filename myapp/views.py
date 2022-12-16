from django.shortcuts import render
from .forms import Register, Login
from django.http import HttpResponseRedirect

# Create your views here.
def index(req):
    return render(req, 'index.html', context={'form': Register, 'form1': Login})

def af_reg(req):
    info = req.POST
    return render(req, 'reg.html', context={'info': info})

def login(req):
    if not Login(req.POST).is_valid():
        return HttpResponseRedirect('/')
    if req.POST['name'] == 'User1' and req.POST['password'] == "12345678":
        return render(req, 'login.html')
    else:
        return HttpResponseRedirect('/')