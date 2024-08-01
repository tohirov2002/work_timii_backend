from django.urls import path
from rest_framework import routers

from users.views import (
    RegisterAPIView,
    ProfileUpdateView,
    password_change_view,
    password_reset_view,
    LoginAPIView,
    LogoutAPIView
)

router = routers.DefaultRouter()
router.register(r'profile', ProfileUpdateView, basename='profile')

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name="register"),
    path('password-change/', password_change_view, name="password-change"),
    path('password-reset/', password_reset_view, name="password-reset"),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
] + router.urls
