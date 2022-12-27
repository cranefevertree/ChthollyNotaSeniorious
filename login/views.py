from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from register import models


# Create your views here.
def index(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        pwd = request.POST.get("pwd")
        if pwd == models.UserInfo.objects.filter(email=email).values()[0]['pwd']:
            return redirect('../')
    return render(request, 'login/index.html')
