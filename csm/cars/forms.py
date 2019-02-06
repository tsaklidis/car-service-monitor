#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms

from django.forms.widgets import TextInput, Select
from csm.cars.models import Car


GEARS = (
    (True, 'Manual'),
    (False, 'Auto'),
)

MOVE = (
    (None, '4X4'),
    (True, 'FWD'),
    (False, 'BCK'),
)


class CarForm(forms.ModelForm):

    brand = forms.CharField(required=True, label='Brand',
                            max_length=25,
                            error_messages={'required': 'Required field'},
                            widget=TextInput(attrs={
                                'class': 'form-control input-sm',
                                'required': 'True',
                                'placeholder': 'Brand, eg: BMW',

                            }))

    kilometers = forms.IntegerField(
        label='Total kilometers',
        error_messages={
            'required': 'Required field',
        },
        required=True,
        widget=TextInput(
            attrs={'class': 'form-control input-sm',
                   'required': 'True',
                   'placeholder': 'eg: 120000',
                   }))

    price = forms.IntegerField(
        label='Price in euro',
        error_messages={
            'required': 'Required field',
        },
        required=True,
        widget=TextInput(
            attrs={'class': 'form-control input-sm',
                   'required': 'True',
                   }))

    hp = forms.IntegerField(
        label='Horse power',
        error_messages={
            'required': 'Required field',
        },
        required=True,
        widget=TextInput(
            attrs={'class': 'form-control input-sm',
                   'required': 'True',
                   'placeholder': 'eg: 120'
                   }))

    cc = forms.IntegerField(
        label='Car Cubic',
        error_messages={
            'required': 'Required field',
        },
        required=True,
        widget=TextInput(
            attrs={'class': 'form-control input-sm',
                   'required': 'True',
                   'placeholder': 'eg: 1300'
                   }))

    gearbox = forms.ChoiceField(
        choices=GEARS, label="Gearbox", required=True,
        widget=forms.Select(
            attrs={'class': 'form-control input-sm'},
        )
    )

    color = forms.CharField(
        label='Main color',
        error_messages={
            'required': 'Required field',
        },
        required=True,
        widget=TextInput(
            attrs={'class': 'form-control input-sm',
                   'required': 'True',
                   'placeholder': 'eg: Red'
                   }))

    euro_type = forms.CharField(
        label='Euro type',
        error_messages={
            'required': 'Required field',
        },
        required=True,
        widget=TextInput(
            attrs={'class': 'form-control input-sm',
                   'required': 'True',
                   'placeholder': 'eg: EURO5'
                   }))

    license_plate = forms.CharField(
        label='License plate',
        error_messages={
            'required': 'Required field',
        },
        required=True,
        widget=TextInput(
            attrs={'class': 'form-control input-sm',
                   'required': 'True',
                   'placeholder': 'eg: KZP1236'
                   }))

    serial = forms.CharField(
        label='Unique serial',
        error_messages={
            'required': 'Required field',
        },
        required=True,
        widget=TextInput(
            attrs={'class': 'form-control input-sm',
                   'required': 'True',
                   'placeholder': 'eg: 19UUB3F77GA001198'
                   }))

    fuel = forms.CharField(
        label='Fuel',
        error_messages={
            'required': 'Required field',
        },
        required=True,
        widget=TextInput(
            attrs={'class': 'form-control input-sm',
                   'required': 'True',
                   'placeholder': 'eg: Gas'
                   }))

    movement = forms.ChoiceField(
        choices=MOVE, label="Movement", required=True,
        widget=forms.Select(
            attrs={'class': 'form-control input-sm'},
        )
    )

    owners_before = forms.IntegerField(
        label='Owners before',
        error_messages={
            'required': 'Required field',
        },
        required=True,
        widget=TextInput(
            attrs={'class': 'form-control input-sm',
                   'required': 'True',
                   'placeholder': 'eg: 1'
                   }))

    airbags = forms.IntegerField(
        label='Airbags',
        error_messages={
            'required': 'Required field',
        },
        required=True,
        widget=TextInput(
            attrs={'class': 'form-control input-sm',
                   'required': 'True',
                   'placeholder': 'eg: 4'
                   }))

    dors = forms.IntegerField(
        label='Dors',
        error_messages={
            'required': 'Required field',
        },
        required=True,
        widget=TextInput(
            attrs={'class': 'form-control input-sm',
                   'required': 'True',
                   'placeholder': 'eg: 4'
                   }))

    class Meta:
        model = Car
        fields = '__all__'
        exluce = ('owner')
