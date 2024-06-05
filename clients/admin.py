from django.contrib import admin
from .models import Client

class ClientAdmin(admin.ModelAdmin):
    list_display = [
        'full_name',
        'contact_method',
    ]

    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    full_name.short_description = 'Client Name'

admin.site.register(Client, ClientAdmin)