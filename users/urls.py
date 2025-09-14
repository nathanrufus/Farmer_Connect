from django.urls import path
from .views import RegisterView, LoginView ,UserProfileUpdateView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', UserProfileUpdateView.as_view(), name='user-profile-update'),
]
