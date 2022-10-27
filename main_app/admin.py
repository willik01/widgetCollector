from django.contrib import admin

# import your models here
from .models import Accessory, Widget, Cleaning

# Register your models here
admin.site.register(Widget)
admin.site.register(Cleaning)
admin.site.register(Accessory)