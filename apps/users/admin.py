from django.contrib import admin
from  apps.users.models import User, Settings

class SettingsFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')

admin.site.register(Settings, SettingsFilterAdmin)
admin.site.register(User)