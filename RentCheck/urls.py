from django.urls import path
from . import views

urlpatterns = [
    path('main_page_rooms', views.main_rooms),
    path('main_page_tenants', views.main_tenants),
    path('start_page', views.start),
    path('my_account', views.account)
]
