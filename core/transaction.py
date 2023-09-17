from django.shortcuts import render, redirect
from core.models import Transaction
from account.models import Account
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def transaction_lists(request):
    sender_transaction = Transaction.objects.filter(sender=request.user).order_by("-id")
    reciever_transaction = Transaction.objects.filter(reciever=request.user).order_by("-id")

    context = {
        "sender_transaction": sender_transaction,
        "reciever_transaction": reciever_transaction,
    }

    return render(request, "transaction/transaction-list.html", context)
