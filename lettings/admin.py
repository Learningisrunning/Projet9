from django.contrib import admin
from lettings.models import Letting
from lettings.models import Address
# Register your models here.

#admin.site.register(Letting)
#admin.site.register(Address)

@admin.register(Address)
class AdressAdmin(admin.ModelAdmin):
    list_display = ('number', 'street','city', 'zip_code')
    ordering = ('city',)
    search_fields = ('city', 'zip_code')
    list_filter = ('city', 'street', 'zip_code', 'number')

@admin.register(Letting)
class LettingAdmin(admin.ModelAdmin):
    list_display = ('title', 'address')
    ordering = ('address',)
    search_fields = ('title', 'address')
    list_filter = ('title', 'address')


