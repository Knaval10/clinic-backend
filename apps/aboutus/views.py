from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import AboutUs
from .serializers import AboutUsSerializer


class AboutUsAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        about_us_content = AboutUs.objects.first()
        if about_us_content:
            serializer = AboutUsSerializer(about_us_content)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"detail": "About Us content not found"},
            status=status.HTTP_404_NOT_FOUND,
        )
