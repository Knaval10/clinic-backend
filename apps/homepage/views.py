from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import HomePage
from .serializers import HomePageSerializer


class HomePageAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        slides = HomePage.objects.all().order_by("id")
        serializer = HomePageSerializer(slides, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = HomePageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
