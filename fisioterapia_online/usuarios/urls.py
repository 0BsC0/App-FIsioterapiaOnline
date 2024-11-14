from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),  # URLs de autenticación predeterminadas de Django
    path('dashboard/', views.user_dashboard, name='dashboard'),  # Página principal del usuario después de iniciar sesión
    path('profile/', views.user_profile, name='user_profile'),  # Perfil del usuario
    path('salir/', views.salir, name='salir'),  # Cerrar sesión
    path('register/', views.register, name='register'),  # Página de registro
    path('login/', views.login_view, name='login'),  # Página de inicio de sesión
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), name='password_reset_complete'),
]
