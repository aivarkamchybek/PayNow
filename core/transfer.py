from django.shortcuts import render, redirect
from account.models import Account
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required

def search_users_account_number(request):
    account = Account.objects.all()
    query = request.POST.get("account_number")
    if query:
        account = account.filter(
        Q(account_number=query)
        )
    context = {
        "account": account,
    }
    return render(request, "transfer/search-user-by-account-number.html", context)
