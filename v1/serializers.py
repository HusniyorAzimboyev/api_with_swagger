from rest_framework import serializers
from .models import Category, Product, Rating
from django.db.models import Avg

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')  # Display category name
    average_rating = serializers.SerializerMethodField()  # Dynamically calculated average rating

    class Meta:
        model = Product
        fields = '__all__'

    def get_average_rating(self, obj):
        """
        This method calculates the average rating for a product.
        It uses the `Rating` model to calculate the average rating dynamically.
        """
        avg_rating = Rating.objects.filter(product=obj).aggregate(Avg('rating'))['rating__avg']
        return round(avg_rating, 2) if avg_rating else 0.0


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
