from django.contrib import admin
from .models import CarShape

@admin.register(CarShape)
class CarShapeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
