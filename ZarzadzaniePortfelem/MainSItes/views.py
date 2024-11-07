from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . models import *

# Create your views here.
def main(request):
    return render(request, 'MainIndex.html')

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')
    context = {'registerform':form}

    return render(request, 'register.html', context=context)

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                return redirect('profile')
    context = {'loginform':form}

    return render(request, 'login.html', context=context)

def logout(request):
    auth.logout(request)

    return redirect("main")

@login_required(login_url="login")
def profile(request):
    return render(request, 'profile.html')

@login_required(login_url="login")
def wallet(request):
    Model_Data = UsersAccount.objects.all()

    return render(request, 'wallet.html', context={
        "variables":Model_Data
    })

@login_required(login_url="login")
def deposit(request, pk):
    if request.method == 'POST':
        deposit = float(request.POST.get('AddMon'))
        total = UsersAccount.objects.get(pk=pk)
        total = total + deposit

        total.save()

    return render(request, 'deposit.html')

@login_required(login_url="login")
def withdraw(request):
    return render(request, 'withdraw.html')