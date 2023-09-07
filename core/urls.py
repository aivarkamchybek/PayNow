from django.urls import path
from core import views
from core import transfer

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),

    #Trasnfers
    path("search-account/", transfer.search_users_account_number, name="search-account"),

]
