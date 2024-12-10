from rest_framework import viewsets
from .models import Category, Product, Rating
from .serializers import CategorySerializer, ProductSerializer, RatingSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def perform_create(self, serializer):
        product = serializer.validated_data['product']
        super().perform_create(serializer)  # Save the rating
        # No need to update product model, calculation is done dynamically in the serializer
