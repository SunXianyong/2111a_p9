from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from drf_spectacular.views import SpectacularSwaggerSplitView
from rest_framework import permissions

schema_view = SpectacularSwaggerSplitView(
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),  # swagger接口文档
]
