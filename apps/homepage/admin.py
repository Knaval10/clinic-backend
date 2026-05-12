from django.contrib import admin

from .models import HomePage


@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ["title", "subtitle", "updated_at"]
    readonly_fields = ["updated_at"]
