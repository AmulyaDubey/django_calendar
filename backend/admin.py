from django.contrib import admin

# Register your models here.

from .models import Profile,Event

admin.site.register(Profile)
admin.site.register(Event)
