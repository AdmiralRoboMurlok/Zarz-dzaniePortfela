from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('profile', views.profile, name="profile"),
    path('logout', views.logout, name="logout"),
    path('wallet', views.wallet, name="wallet"),
    path('deposit/<int:pk>', views.deposit, name="deposit"),
    path('withdraw/<int:pk>', views.withdraw, name="withdraw"),
    path('bank/<int:pk>', views.bank, name="bank"),
    path('payback/<int:pk>', views.payback, name="payback"),
    path('failure', views.failure, name="failure")
]
