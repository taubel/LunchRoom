from django.contrib import admin

from .models import Room, User, FoodItem


admin.site.register(Room)
admin.site.register(User)
admin.site.register(FoodItem)
