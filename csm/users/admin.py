from django.contrib import admin

from csm.users.models import Owner


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    model = Owner
    list_display = ('last_name', 'email', 'serial', 'company')
