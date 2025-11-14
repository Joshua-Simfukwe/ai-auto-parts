from rest_framework import generics
from .models import PartCategory, Part
from .serializers import PartCategorySerializer, PartSerializer
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView

class PartCategoryListCreateView(generics.ListCreateAPIView):
    queryset = PartCategory.objects.all()
    serializer_class = PartCategorySerializer


class PartListCreateView(generics.ListCreateAPIView):
    queryset = Part.objects.all()
    serializer_class = PartSerializer


class CategoryChildrenView(generics.ListAPIView):
    serializer_class = PartCategorySerializer

    def get_queryset(self):
        parent_id = self.kwargs.get("pk")
        return PartCategory.objects.filter(parent_id=parent_id)

class PartSearchView(APIView):
    """
    Basic text-based search.
    Matches name, brand, category.
    """

    def get(self, request):
        query = request .GET.get("q", "").strip()

        if not query:
            return Response({"results": []})
        
        parts = Part.objects.filter(
            Q(name__icontains=query) |
            Q(brand__icontains=query) |
            Q(category__name__icontains=query)
         )
        
        serializer = PartSerializer(parts, many=True)
        return Response({"results": serializer.data})

