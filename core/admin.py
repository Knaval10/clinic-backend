from django.contrib import admin
from .models import HomePage, Doctor, Testimonial, ContactMessage, Service, AboutUs, Milestone, Leader

@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'updated_at']
    # Display JSON as pretty text in the admin
    readonly_fields = ['updated_at']
    
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("name", "highest_degree", "nmc_number", "years_of_experience", "order", "slug")
    list_editable = ("order",)
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "highest_degree", "nmc_number", "leadership_role")

class ServiceInline(admin.StackedInline):
    model = Service
    fk_name = "parent"
    extra = 1
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "parent", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "description")
    list_filter = ("parent",)
    inlines = [ServiceInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "parent":
            kwargs["queryset"] = Service.objects.filter(parent__isnull=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "designation", "is_approved", "created_at")
    list_filter = ("is_approved",)
    actions = ["approve_testimonials"]

    def approve_testimonials(self, request, queryset):
        queryset.update(is_approved=True)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone", "created_at")

class MilestoneInline(admin.TabularInline):
    model = Milestone
    extra = 1

class LeaderInline(admin.StackedInline):
    model = Leader
    extra = 1

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated_at']
    readonly_fields = ['updated_at']
    inlines = [MilestoneInline, LeaderInline]
