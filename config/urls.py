from django.contrib import admin
from django.urls import path, include 

# Import for routers 
from rest_framework.routers import DefaultRouter 

# Import for APIs 
from user.views import UserProfileViewSet, UserViewSet
from product.views import ProductViewSet
from category.views import CategoryViewSet 
from cart.views import CartViewSet 
from order.views import OrderViewSet 
from review.views import ReviewViewSet
from brand.views import BrandViewSet 
from cartitem.views import CartItemViewSet

# Import for swagger 
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Import for simplejwt
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Routers
router = DefaultRouter() 
router.register(r'user', UserViewSet, basename='User') # User API
router.register(r'userprofile', UserProfileViewSet, basename='User_Profile') # UserProfile API
router.register(r'product', ProductViewSet, basename='Product') # Product API 
router.register(r'category', CategoryViewSet, basename='Category') # Category API 
router.register(r'cart', CartViewSet, basename='Cart') # Cart API
router.register(r'cartitem', CartItemViewSet, basename='CartItem') # CartItem API
router.register(r'order', OrderViewSet, basename='Order') # Order API
router.register(r'review', ReviewViewSet, basename='Review') # Review API
router.register(r'brand', BrandViewSet, basename='Brand') # Brand API

# Swagger Setting
schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@myapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Authentication routes
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # App Routers
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger',cache_timeout=0), name='schema-swagger-ui'),
    path('user/', include('user.urls')),
    path('product/', include('product.urls')),      
    path('category/', include('category.urls')),
    path('review/', include('review.urls')),
    path('cart/', include('cart.urls')), 
    path('cartitem/', include('cartitem.urls')),
    path('order/', include('order.urls')),
    path('brand/', include('brand.urls')),

    # Router urls
    path('', include(router.urls)),
] 