from django.contrib import admin
from . models import FRBS, UsersAccount, Bank, Histroy

# Register your models here.
admin.site.register(FRBS)
admin.site.register(UsersAccount)
admin.site.register(Bank)
admin.site.register(Histroy)