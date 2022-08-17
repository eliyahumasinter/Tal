from django.contrib import admin

# Register your models here.
from .models import Email, Card, Event

admin.site.register(Card)
admin.site.register(Email)
admin.site.register(Event)
