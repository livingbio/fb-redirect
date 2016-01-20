from django.contrib import admin
from .models import Redirect, ClickLog

# Register your models here.

class RedirectAdmin(admin.ModelAdmin):
    list_display = ('short', 'url')

class ClickLogAdmin(admin.ModelAdmin):
    list_display = ('url', 'ip', 'created')

admin.site.register(Redirect, RedirectAdmin)
admin.site.register(ClickLog, ClickLogAdmin)
