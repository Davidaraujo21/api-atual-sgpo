from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from main.views import CustomTokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
    path('docs/',include("api_docs.urls")),
    path('api/login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('api/refresh/', TokenRefreshView.as_view(), name='refresh')
] 

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
