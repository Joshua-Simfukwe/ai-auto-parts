from django.urls import path
from .views import (
    PartCategoryListCreateView,
    PartListCreateView,
    CategoryChildrenView,
)

urlpatterns = [
    path("categories/", PartCategoryListCreateView.as_view(), name="category-list"),
    path("categories/<int:pk>/children/", CategoryChildrenView.as_view(), name="category-children"),
    path("parts/", PartListCreateView.as_view(), name="part-list"),
]
