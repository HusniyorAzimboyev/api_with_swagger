from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, RatingViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'ratings', RatingViewSet, basename='rating')

urlpatterns = router.urls
