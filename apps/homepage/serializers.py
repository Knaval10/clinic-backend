from rest_framework import serializers

from .models import HomePage


class HomePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePage
        fields = ["id", "title", "subtitle", "description", "banner_image", "updated_at"]
