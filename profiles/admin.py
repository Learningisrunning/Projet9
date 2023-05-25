from django.contrib import admin
from profiles.models import Profile
# Register your models here.

#admin.site.register(Profile)


@admin.register(Profile)
class LettingAdmin(admin.ModelAdmin):
    list_display = ('user', 'favorite_city')
    ordering = ('user',)
    search_fields = ('user', 'favorite_city')
    list_filter = ('user', 'favorite_city')
