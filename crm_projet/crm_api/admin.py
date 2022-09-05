from django.contrib import admin
from . import models


class EventStatusAdmin(admin.ModelAdmin):
    list_display = ["status"]


admin.site.register(models.Client)
admin.site.register(models.Contract)
admin.site.register(models.Event)
admin.site.register(models.Event_status, EventStatusAdmin)
