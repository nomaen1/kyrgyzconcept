from django.urls import path, reverse
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
#my imports
from apps.users import views


urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.user_login, name="login"),
    path('profile/<int:id>/', views.profile, name="profile"),
    path("logout/", LogoutView.as_view(next_page = "login"), name = "logout"),
    
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]

