from django.urls import path
from core import views
from core import transfer

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),

    #Trasnfers
    path("search-account/", transfer.search_users_account_number, name="search-account"),
    path("amount-transfer/<account_number>/", transfer.AmountTransfer, name="amount-transfer"),
    path("amount-transfer-process/<account_number>/", transfer.AmountTransferProcess, name="amount-transfer-process"),
    path("transfer-confirmation/<account_number>/<transaction_id>", transfer.TransferConfirmation, name="transfer-confirmation"),

]
