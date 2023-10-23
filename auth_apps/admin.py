from django.contrib import admin

from auth_apps.models import Profile



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'location', 'profile_image', 'profile_type','created']
