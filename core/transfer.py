from django.shortcuts import render, redirect
from account.models import Account
from django.contrib.auth.decorators import login_required

@login_required

def search_users_account_number(request):
    return render(request, "transfer/search-user-by-account-number.html")