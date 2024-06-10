from django.urls import path

from .views import logout_view, login_view, sign_up, verify_code

app_name = 'account'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', sign_up, name='register'),
    path('verify-code', verify_code, name='verify_code'),
]
