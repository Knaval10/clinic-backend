from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.decorators import api_view

from .models import HomePage, Testimonial, Doctor, Service, AboutUs
from .serializers import HomePageSerializer, TestimonialSerializer, DoctorOverviewSerializer, DoctorDetailSerializer, Service, ServiceSerializer, ContactMessageSerializer, AboutUsSerializer


class HomePageAPIView(APIView):
    authentication_classes = []  # public
    permission_classes = []      # public

    def get(self, request):
        slides = HomePage.objects.all().order_by('id')  # fetch all slides
        serializer = HomePageSerializer(slides, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Add a new slide
        """
        serializer = HomePageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TestimonialListAPIView(generics.ListAPIView):
    queryset = Testimonial.objects.filter(is_approved=True).order_by('-created_at')
    serializer_class = TestimonialSerializer
    authentication_classes = []  # public
    permission_classes = []      # public

# List of all doctors (overview)
class DoctorListAPIView(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorOverviewSerializer
    authentication_classes = []
    permission_classes = []

# Details of single doctor
class DoctorDetailAPIView(generics.RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorDetailSerializer
    lookup_field = "slug"  # fetch by slug instead of pk
    authentication_classes = []
    permission_classes = []

class ServiceListAPIView(generics.ListAPIView):
    queryset = Service.objects.filter(parent__isnull=True)
    serializer_class = ServiceSerializer
    authentication_classes = []  # no auth
    permission_classes = []      # open to everyone

# Detail content for a menu/submenu
class ServicesDetailAPIView(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = "slug"  # fetch by menu slug
    authentication_classes = []
    permission_classes = []

@api_view(['POST'])
def contact_message_create(request):
    serializer = ContactMessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "Message sent successfully!"},
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AboutUsAPIView(APIView):
    authentication_classes = []  # public
    permission_classes = []      # public

    def get(self, request):
        about_us_content = AboutUs.objects.first()
        if about_us_content:
            serializer = AboutUsSerializer(about_us_content)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"detail": "About Us content not found"}, status=status.HTTP_404_NOT_FOUND)