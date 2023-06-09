from django.urls import path
from users import views
from django_ratelimit.decorators import ratelimit

urlpatterns = [
    path('register/', views.RegistationView.as_view(), name='register'),
    path('profile_edit/', views.ProfileEditView.as_view(), name='profile_edit'),
    path('password/', ratelimit(key='ip', method='POST', rate='2/m')(views.ChangePassword1View.as_view(template_name="registration/change_password.html"))),
    path('password_changed/', views.change_password, name='password_changed'),
    path('<int:pk>/profile/', views.ShowProfileView.as_view(), name='show_profile'),
    path('<int:pk>/edit_profile/', views.EditProfileview.as_view(), name='edit_profile_user'),
    path('create_user_profile/', views.CreateProfileView.as_view(), name='create_user_profile'),
    path('about/', views.aboutView, name='about'),

    path('login/', views.login_view, name='login'),
]