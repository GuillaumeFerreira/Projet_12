from django.contrib import admin
from . import models




class EventAdmin(admin.ModelAdmin):
    list_display = ('id',  'notes', 'client', 'employee_event')

admin.site.register(models.Client)
admin.site.register(models.Contract)
admin.site.register(models.Event,EventAdmin)
admin.site.register(models.Employee)
