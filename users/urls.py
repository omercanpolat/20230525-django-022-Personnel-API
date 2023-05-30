from django.urls import path, include
from .views import RegisterView, ProfileUpdateView, logout


urlpatterns = [
    path('auth/logout/', logout),
    path('auth/', include('dj_rest_auth.urls')),
    path('register/', RegisterView.as_view()),
    path('profile/<int:pk>/', ProfileUpdateView.as_view()),
]
