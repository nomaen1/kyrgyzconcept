from django.contrib import admin
#my imports
from apps.jobs import models

# Register your models here.
class JobAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'created_at')
    search_fields = ('title', )

class CategoryAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title',)
    search_fields = ('title',)

class ReadyCVAdmin(admin.ModelAdmin):
    list_display = ('user', )
    search_fields = ('user', )

admin.site.register(models.Jobs, JobAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.CV)
admin.site.register(models.ReadyCV, ReadyCVAdmin)


