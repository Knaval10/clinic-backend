from django.contrib import admin
from .models import HomePage, Doctor, Testimonial, ContactMessage, Services, ServicesMenus

@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ("title", "updated_at")

    # Allow only one HomePage instance
    def has_add_permission(self, request):
        if HomePage.objects.exists():
            return False
        return True
    
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("name", "highest_degree", "years_of_experience", "slug")
    prepopulated_fields = {"slug": ("name",)}

@admin.register(ServicesMenus)
class ServicesMenusAdmin(admin.ModelAdmin):
    list_display = ("name", "parent", "slug")
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ("menu",)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "designation", "is_approved", "created_at")
    list_filter = ("is_approved",)
    actions = ["approve_testimonials"]

    def approve_testimonials(self, request, queryset):
        queryset.update(is_approved=True)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
