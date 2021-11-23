from django.contrib import admin

from meetings import models

admin.site.register(models.Room)
admin.site.register(models.Meeting)
