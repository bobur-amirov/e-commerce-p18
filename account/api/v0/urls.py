from django.urls import path

from .views import SignUp, UserUpdateAPIView



urlpatterns = [
    path('register/', SignUp.as_view(), name='register'),
    path('update-profile/<int:pk>', UserUpdateAPIView.as_view(), name='update_profile')
]