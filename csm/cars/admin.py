from django.contrib import admin

from csm.cars.models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    model = Car
    list_display = ('brand', 'id', 'owner')
