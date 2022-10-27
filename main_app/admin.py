from django.contrib import admin

# import your models here
from .models import Widget, Cleaning

# Register your models here
admin.site.register(Widget)
admin.site.register(Cleaning)