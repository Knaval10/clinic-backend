from rest_framework import serializers

from .models import AboutUs, Leader, Milestone


class MilestoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milestone
        fields = ["id", "year", "event"]


class LeaderSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True, required=False)

    class Meta:
        model = Leader
        fields = ["id", "name", "role", "image", "nmc_number", "description"]


class AboutUsSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True, required=False)
    milestones = MilestoneSerializer(many=True, read_only=True)
    leaders = LeaderSerializer(many=True, read_only=True)

    class Meta:
        model = AboutUs
        fields = [
            "id", "title", "description", "image",
            "journey_title", "journey_subtitle", "journey_description",
            "updated_at", "milestones", "leaders",
        ]
