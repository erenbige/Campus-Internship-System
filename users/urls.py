from django.urls import path
from .views import UserRegistrationView, CustomLoginView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
]