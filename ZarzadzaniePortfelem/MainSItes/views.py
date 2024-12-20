from django.shortcuts import render, redirect, get_object_or_404
from . forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . models import *
from django.db.models import F
from django.contrib import messages
import datetime

placeholder_int = 0
placeholder_string = ""

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
    context = {
        'pk': request.user.pk
    }
    return render(request, 'profile.html', context)

@login_required(login_url="login")
def wallet(request):
    Model_Data = UsersAccount.objects.all()
    local_history = Histroy.objects.all()

    context = {
        'pk': request.user.pk,
        'variables': Model_Data,
        'history': local_history
    }

    return render(request, 'wallet.html', context)

@login_required(login_url="login")
def deposit(request, pk):
    context = {
        'pk': request.user.pk
    }

    if request.method == 'POST':
        deposit_amount = float(request.POST.get('AddMon'))
        user_acc = get_object_or_404(UsersAccount, id=pk)

        user_acc.balance = F('balance') + deposit_amount
        user_acc.save()

        history = Histroy()
        name = f"Dodano {deposit_amount} do konta"
        date = datetime.datetime.now()

        history.name = name
        history.date = date
        history.save()


        user_acc.refresh_from_db()
        history.refresh_from_db()
        messages.success(request, "Money has been added to your account")
        return redirect(wallet)

    return render(request, 'deposit.html', context)

@login_required(login_url="login")
def withdraw(request, pk):
    context = {
        'pk': request.user.pk
    }
    if request.method == 'POST':
        withdraw_amount = float(request.POST.get('Withdraw'))
        user_acc = get_object_or_404(UsersAccount, id=pk)

        if user_acc.balance >= withdraw_amount:
            user_acc.balance = F('balance') - withdraw_amount
            user_acc.save()

            history = Histroy()
            name = f"Zabrano {withdraw_amount} z konta"
            date = datetime.datetime.now()

            history.name = name
            history.date = date
            history.save()

            user_acc.refresh_from_db()
            history.refresh_from_db()
            return redirect(wallet)
        else:
            return redirect(failure)

    return render(request, 'withdraw.html', context)

@login_required(login_url="login")
def bank(request, pk):
    bank_model = Bank.objects.all()

    if request.method == 'POST':
        loan_amount = float(request.POST.get('takeloan'))
        user_acc = get_object_or_404(UsersAccount, id=pk)
        bank_acc = get_object_or_404(Bank, id=pk)

        if bank_acc.balance >= loan_amount:
            user_acc.borrowed = F('borrowed') + loan_amount
            user_acc.save()
            user_acc.refresh_from_db()

            bank_acc.balance = F('balance') - loan_amount
            bank_acc.save()
            bank_acc.refresh_from_db()

            history = Histroy()
            name = f"Wziąłeś {loan_amount} długu"
            date = datetime.datetime.now()

            history.name = name
            history.date = date
            history.save()

            user_acc.refresh_from_db()
            history.refresh_from_db()

            return redirect(wallet)
        else:
            return redirect(failure)

    return render(request, "bank.html", context={
        'pk': request.user.pk,
        'bank': bank_model
    })

@login_required(login_url="login")
def payback(request, pk):
    if request.method == 'POST':
        payback_amount = float(request.POST.get('payback'))
        user_acc = get_object_or_404(UsersAccount, id=pk)
        bank_acc = get_object_or_404(Bank, id=pk)

        if user_acc.borrowed >= payback_amount:
            user_acc.borrowed = F('borrowed') - payback_amount
            user_acc.save()
            user_acc.refresh_from_db()

            bank_acc.loans = F('loans') - payback_amount
            bank_acc.balance = F('balance') + payback_amount
            bank_acc.save()
            bank_acc.refresh_from_db()

            history = Histroy()
            name = f"Spłaciłeś {payback_amount} długu"
            date = datetime.datetime.now()

            history.name = name
            history.date = date
            history.save()

            user_acc.refresh_from_db()
            history.refresh_from_db()

            return redirect(wallet)
        else:
            return redirect(failure)

    return render(request, "payback.html", context={
        'pk': request.user.pk
    })

@login_required(login_url="login")
def failure(request):
    return render(request, "failure.html",  context = {'pk': request.user.pk,})