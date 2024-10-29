from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'MainIndex.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def dashboard(request):
    pass