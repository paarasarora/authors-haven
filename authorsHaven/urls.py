from django.conf import settings
from django.contrib import admin
from django.urls import path,include,re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from core_apps.users.urls import router as accounts_router

schema_view = get_schema_view(
    openapi.Info(
        title="Authors API",
        default_version="v1",
        description="API endpoints for the Authors API course",
        contact=openapi.Contact(email="paarasarora2@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.registry.extend(accounts_router.registry)

urlpatterns = [
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path(settings.ADMIN_URL, admin.site.urls),
    re_path('api/v1/', include(router.urls)),
    re_path('api/v1/', include('core_apps.users.urls', namespace='users')),
    path("api/v1/profiles/", include("core_apps.profiles.urls")),
    path("api/v1/articles/", include("core_apps.articles.urls")),
    path("api/v1/ratings/", include("core_apps.ratings.urls")),
]
