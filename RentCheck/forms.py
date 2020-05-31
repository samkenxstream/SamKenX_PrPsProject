from .models import Rooms, Tenant
from django.forms import ModelForm, TextInput


class RoomForm(ModelForm):
    class Meta:
        model = Rooms

        fields = ['country',
                  'city',
                  'street',
                  'house_number',
                  'room_area',
                  'basement_area',
                  'basement_ratio',
                  'KT',
                  'author_id']

        widgets = {
            'country': TextInput(attrs={
                'class': 'form-control',
                'name': 'country',
                'id': 'country',
                'placeholder': 'Введите страну'}),

            'city': TextInput(attrs={
                'class': 'form-control',
                'name': 'city',
                'id': 'city',
                'placeholder': 'Введите город'
            }),

            'street': TextInput(attrs={
                'class': 'form-control',
                'name': 'street',
                'id': 'street',
                'placeholder': 'Введите улицу'
            }),

            'house_number': TextInput(attrs={
                'class': 'form-control',
                'name': 'number',
                'id': 'number',
                'placeholder': 'Введите номер дома'
            }),

            'room_area': TextInput(attrs={
                'class': 'form-control',
                'name': 'area',
                'id': 'area',
                'placeholder': 'Введите площадь'
            }),

            'basement_area': TextInput(attrs={
                'class': 'form-control',
                'name': 'basement area',
                'id': 'basement area',
                'placeholder': 'Введите площадь подвала'
            }),

            'basement_ratio': TextInput(attrs={
                'class': 'form-control',
                'name': 'basement ratio',
                'id': 'basement ratio',
                'placeholder': 'Введите коэффициент подвала'
            }),

            'KT': TextInput(attrs={
                'class': 'form-control',
                'name': 'KR',
                'id': 'KT',
                'placeholder': 'Введите KT'
            })
        }
