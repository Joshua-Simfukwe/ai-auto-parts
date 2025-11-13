from django.contrib import admin
from .models import CarShape, PartCategory, Part

@admin.register(CarShape)
class CarShapeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

@admin.register(PartCategory)
class PartCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "parent")
    list_filter = ("parent",)
    search_fields = ("name",)

@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "brand", "category")
    list_filter = ("brand", "category")
    search_fields = ("name", "brand")    
