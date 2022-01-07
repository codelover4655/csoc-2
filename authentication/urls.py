from django.urls import path
from .views import RegisterView, UserProfileView,LoginView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('profile/', UserProfileView.as_view()),
]