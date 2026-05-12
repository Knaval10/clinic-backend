from django.contrib import admin

from .models import AboutUs, Leader, Milestone


class MilestoneInline(admin.TabularInline):
    model = Milestone
    extra = 1


class LeaderInline(admin.StackedInline):
    model = Leader
    extra = 1


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ["title", "updated_at"]
    readonly_fields = ["updated_at"]
    inlines = [MilestoneInline, LeaderInline]
