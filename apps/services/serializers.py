from rest_framework import serializers

from .models import Service


class ServiceSerializer(serializers.ModelSerializer):
    sub_services = serializers.SerializerMethodField()
    title = serializers.CharField(source="name", read_only=True)

    class Meta:
        model = Service
        fields = [
            "id", "name", "slug", "parent",
            "description", "image", "extra_info", "sub_services", "title",
        ]

    def get_sub_services(self, obj):
        children = obj.sub_services.all()
        return ServiceSerializer(children, many=True).data
