from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from docs_data import views

router = routers.DefaultRouter()
router.register(r'regions', views.RegionViewSet)
router.register(r'subdivisions', views.SubdivisionViewSet)
router.register(r'categories', views.CategoryItemViewSet)
router.register(r'categories-client', views.CategoryItemViewSetClient)
router.register(r'docs', views.DocDataViewSet)
router.register(r'docs-client', views.DocDataViewSetClient)
router.register(r'users', views.CustomUserViewSet)

urlpatterns = [
    path('', RedirectView.as_view(url='/api')),
    path('api/users/me/', views.get_me),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
