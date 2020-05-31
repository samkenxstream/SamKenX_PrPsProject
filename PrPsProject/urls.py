from django.contrib import admin
from django.urls import path, include
from RentCheck.views import start


urlpatterns = [
    path('', start),
    path('admin/', admin.site.urls),
    path('RentCheck/', include('RentCheck.urls')),
    path('grappelli/', include('grappelli.urls')),
    path('accounts/', include('allauth.urls'))
]
