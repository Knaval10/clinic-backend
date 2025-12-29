from rest_framework import serializers
from .models import HomePage, Testimonial, Services, ServicesMenus, Doctor


class HomePageSerializer(serializers.ModelSerializer):
    banner_image = serializers.ImageField(use_url=True)

    class Meta:
        model = HomePage
        fields = [
            "title",
            "subtitle",
            "description",
            "banner_image",
            "updated_at",
        ]

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

class ServicesSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True, required=False)

    class Meta:
        model = Services
        fields = ["menu", "description", "image", "extra_info"]

class SubMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesMenus
        fields = ["id", "name", "slug"]

class ServicesMenusSerializer(serializers.ModelSerializer):
    sub_menus = SubMenuSerializer(many=True, read_only=True)

    class Meta:
        model = ServicesMenus
        fields = ["id", "name", "slug", "sub_menus"]