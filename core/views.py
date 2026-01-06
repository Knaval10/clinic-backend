from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from .models import HomePage, Testimonial, Doctor, ServicesMenus, Services
from .serializers import HomePageSerializer, TestimonialSerializer, DoctorOverviewSerializer, DoctorDetailSerializer, ServicesMenusSerializer, ServicesSerializer


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

# List all top-level menus with submenus
class ServicesMenusListAPIView(generics.ListAPIView):
    queryset = ServicesMenus.objects.filter(parent__isnull=True)
    serializer_class = ServicesMenusSerializer
    authentication_classes = []
    permission_classes = []

# Detail content for a menu/submenu
class ServicesDetailAPIView(generics.RetrieveAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    lookup_field = "menu__slug"  # fetch by menu slug
    authentication_classes = []
    permission_classes = []