from django.contrib import admin
from  apps.users.models import User, Settings

class SettingsFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')

admin.site.register(Settings, SettingsFilterAdmin)

class UserAdmin(admin.ModelAdmin):
    list_filter = ("fullname", )
    list_display = ("fullname", )
    search_fields = ("fullname", )
    
admin.site.register(User)