from rest_framework import serializers
from .models import HomePage, Testimonial, Service, Doctor, ContactMessage

class HomePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePage
        fields = ['id', 'title', 'subtitle', 'description', 'banner_image', 'updated_at']

class TestimonialSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True, required=False)

    class Meta:
        model = Testimonial
        fields = ["name", "designation", "message", "image", "created_at"]

class DoctorOverviewSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Doctor
        fields = ["id", "name", "image", "highest_degree", "years_of_experience", "slug"]

class DoctorDetailSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Doctor
        fields = ["id", "name", "image", "highest_degree", "years_of_experience", "details", "slug"]

class ServiceSerializer(serializers.ModelSerializer):
    sub_services = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = [
            "id", "name", "slug", "parent",
            "description", "image", "extra_info", "sub_services"
        ]

    def get_sub_services(self, obj):
        children = obj.sub_services.all()
        return ServiceSerializer(children, many=True).data

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['id', 'name', 'email', 'subject', 'message', 'created_at']