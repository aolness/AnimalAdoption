from django.apps import apps
from .serializers import (
    AnimalSerializer,
    NewsSerializer,
    SpeciesSerializer,
    BreedSerializer,
    SizeSerializer,
    AvailabilitySerializer,
    DispositionSerializer,
    UserSerializer
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.pagination import LimitOffsetPagination
from django.contrib.auth.models import User

class FindAnimalsView(APIView):
    """
    GET list of all animals.

    Alternatively, use POST to request animals that match specified filter
    options.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = apps.get_model("animals", "Animal").objects.all()
        serializer = AnimalSerializer(queryset, many=True)

        return Response(serializer.data, status=200)

    def post(self, request):
        data = request.data
        queryset = apps.get_model("animals", "Animal").objects.filter(**data)
        serializer = AnimalSerializer(queryset, many=True)
        
        return Response(serializer.data, status=200)

class NewsListView(ListAPIView):
    """
    Get list of news. Pagination is enabled.

    Possible examples of how this can be used:
    127.0.0.1:8000/api/news/
    127.0.0.1:8000/api/news/?limit=1&offset=6
    127.0.0.1:8000/api/news/?limit=3
    """
    
    permission_classes = [IsAuthenticated]
    queryset = apps.get_model("news", "News").objects.all()
    serializer_class = NewsSerializer
    pagination_class = LimitOffsetPagination


class AnimalOptionsView(APIView):
    """
    Get all possible filter options that can be used for animals.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        species = apps.get_model("animals", "Species").objects.all()
        breeds = apps.get_model("animals", "Breed").objects.all()
        sizes = apps.get_model("animals", "Size").objects.all()
        availabilities = apps.get_model("animals", "Availability").objects.all()
        dispositions = apps.get_model("animals", "Disposition").objects.all()

        species_serializer = SpeciesSerializer(species, many=True)
        breed_serializer = BreedSerializer(breeds, many=True)
        size_serializer = SizeSerializer(sizes, many=True)
        availability_serializer = AvailabilitySerializer(availabilities, many=True)
        disposition_serializer = DispositionSerializer(dispositions, many=True)

        return Response({
            "species": species_serializer.data,
            "breeds": breed_serializer.data,
            "sizes": size_serializer.data,
            "availabilities": availability_serializer.data,
            "dispositions": disposition_serializer.data,
        })

class UserCreateView(CreateAPIView):
    """
    Only used for user registration
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer