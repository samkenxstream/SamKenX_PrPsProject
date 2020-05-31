from django.shortcuts import render
from .models import Rooms, Tenant
from .forms import RoomForm
from django.http import HttpResponseRedirect
from allauth.account.views import *
from django.contrib.auth.decorators import user_passes_test


def user_is_tenant(user):
    return user.groups.filter(name='Tenant').exists()


def user_is_landlord(user):
    return user.groups.filter(name='Landlord').exists()


def count_rent(room_area, basement_area, basement_ratio, KT, base_rate=17.58):
    return round((base_rate / 12 * room_area + base_rate / 12 * basement_area * basement_ratio) * KT, 4)


#@user_passes_test(user_is_landlord)
def main_rooms(request):
    rooms = {}
    form = {}

    if request.user.email == 'Egor.Shilkin2000@yandex.ru':
        rooms = Rooms.objects.filter(author_id=request.user.id)

        if request.method == 'POST':
            form = RoomForm(request.POST)

            if form.is_valid():
                thought = form.save(commit=False)
                thought.author_id = request.user.id
                thought.save()

                return HttpResponseRedirect("/RentCheck/main_page_rooms")

        form = RoomForm()



    if request.user.is_staff:
        rooms = Rooms.objects.all()

        if request.method == 'POST':
            form = RoomForm(request.POST)

            if form.is_valid():
                thought = form.save(commit=False)
                thought.author_id = request.user.id
                thought.save()

                return HttpResponseRedirect("/RentCheck/main_page_rooms")

        form = RoomForm()


    if request.user.email == 'egor.shilkin@icloud.com':
        rooms = Rooms.objects.filter(tenant_email=request.user.email)


    all_rooms = []

    for room in rooms:
        room_info = {
                    'country': room.country,
                    'city': room.city,
                    'street': room.street,
                    'house_number': room.house_number,

                    'room_area': room.room_area,
                    'basement_area': room.basement_area,
                    'basement_ratio': room.basement_ratio,
                    'KT': room.KT,
                    'rent': count_rent(room.room_area, room.basement_area, room.basement_ratio, room.KT),
                    'tenant_email': room.tenant_email
                   }

        all_rooms.append(room_info)


    context = {'all_info': all_rooms, 'form': form}

    return render(request, "main_page_rooms.html", context)


def main_tenants(request):
    tenants = Tenant.objects.all()

    all_tenants = []

    for tenant in tenants:
        tenant_info = {
                    'name': tenant.name,
                    'surname': tenant.surname,
                    'middle_name': tenant.middle_name,
                    'rented_rooms_count': tenant.rented_rooms_count,
                    'rented_rooms': tenant.rented_room,
                   }

        all_tenants.append(tenant_info)

    context = {'all_tenants': all_tenants}

    return render(request, "main_page_tenants.html", context=context)


def start(request):
    return render(request, 'start_page.html')


def account(request):
    return render(request, 'my_account.html')
