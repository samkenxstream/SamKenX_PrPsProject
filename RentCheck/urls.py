from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('start_page', views.start)
]
