from django.urls import path

from .views import UserRegisterView, CustomLoginView, CustomLogoutView, ProfileView, AvatarUpdateView, ProfileUpdateView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path("profile/edit/", ProfileUpdateView.as_view(), name="edit_profile"),
    path('update-avatar/', AvatarUpdateView.as_view(), name='avatar-update'),
]
