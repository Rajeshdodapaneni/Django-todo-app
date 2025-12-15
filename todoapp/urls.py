from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    # path('delete-task/<str:name>/', views.DeleteTask, name='delete'),
    path('finish-task/<int:id>/', views.FinishTask, name='finish_task'),

    path('delete-task/<int:id>/', views.DeleteTask, name='delete_task'),
    path('update-task/<int:id>/', views.Update, name='update_task'),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('loginview/', views.login_view, name='loginview'),
    path('registerview/', views.register_view, name='registeviewr'),

    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),

]