from django.contrib import admin
from django.urls import path, include
from api.views import CreateUserView, password_reset_request, password_reset_confirm
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/user/register/", CreateUserView.as_view(), name="register"),
    path("api/token/", TokenObtainPairView.as_view(), name="get_token"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh_token"),
    path("api/password-reset/", password_reset_request, name="password_reset"),
    path(
        "api/password-reset-confirm/",
        password_reset_confirm,
        name="password_reset_confirm",
    ),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include("api.urls")),
]
