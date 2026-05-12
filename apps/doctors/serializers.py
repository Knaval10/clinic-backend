from rest_framework import serializers

from .models import Doctor


class DoctorOverviewSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Doctor
        fields = [
            "id", "name", "image", "highest_degree",
            "nmc_number", "years_of_experience", "order", "slug",
        ]


class DoctorDetailSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Doctor
        fields = [
            "id", "name", "image", "highest_degree",
            "nmc_number", "years_of_experience", "order", "details", "slug",
        ]
