from django.shortcuts import render
from .models import table


def index(request):
    table_elements = table.objects.order_by('name')[:5]
    return render(request, 'table.html', {'table_elements': table_elements})


def start(request):
    return render(request, 'start_page.html')
