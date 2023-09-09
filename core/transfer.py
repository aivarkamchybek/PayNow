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
        Q(account_number=query) |
        Q(account_id=query) 
        ).distinct()
    context = {
        "account": account,
        "query": query,
    }
    return render(request, "transfer/search-user-by-account-number.html", context)

def AmountTransfer(request, account_numbber):
    return render(request, "transfer/amount-transfer.html")