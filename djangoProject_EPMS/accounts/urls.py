from django.urls import path, include

from djangoProject_EPMS.accounts.views import (
    RegisterUserView, LoginUserView, LogoutUserView,
    UserProfileView, UserProfileEditView, DeleteUserProfileView
)

urlpatterns = (
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),

    path('profile/<int:pk>/', include([
        path('', UserProfileView.as_view(), name='profile'),
        path('edit/', UserProfileEditView.as_view(), name='edit_profile'),
        path('delete/', DeleteUserProfileView.as_view(), name='delete_profile'),
    ])),
)
