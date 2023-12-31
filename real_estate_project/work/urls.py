from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(
            redirect_authenticated_user=True,
            template_name="registration/login.html",
            success_url="home",
        ),
        name="login",
    ),
    path(
        "signup/",
        views.SignUpView.as_view(template_name="registration/signup.html"),
        name="signup",
    ),
    # Forget Password
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name="password-reset/password_reset.html",
            subject_template_name="password-reset/password_reset_subject.txt",
            email_template_name="password-reset/password_reset_email.html",
            success_url="/login/",
        ),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="password-reset/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="password-reset/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="password-reset/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]
