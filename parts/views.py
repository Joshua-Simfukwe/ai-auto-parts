from rest_framework import generics
from .models import PartCategory, Part
from .serializers import PartCategorySerializer, PartSerializer

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
