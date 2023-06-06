from django.urls import path 
from . import views 
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('', views.welcome, name="home"),
    path('login/', views.logPage, name="login"),
    path('logout/', views.LogOut, name="logout"),
    path('registration/', views.reg, name="registration"),

    path('profile/', views.profile, name='profile'),
    path('account_settings/', views.acc_settings, name='account_settings'),
    # path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    # path('reset_password_done/', auth_views.PasswordResetDoneView.as_view(), name='done_password'),
    # path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='confirm_password'),
    # path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='complete_password'),


    path('upload_files/', views.file_up, name='uploadfile'),
    path('delete_file/<int:pk>', views.delete_file, name='delete_file'),

    path('history/<str:top>', views.history, name='history'),


    path('category/<str:cat_s>/', views.categories, name='category'),
 
 
    path('results/', views.results, name='results'),
    path('update_files/<int:id>', views.update_file, name='update'),
    # path('view_file/', views.read_file, name='view_file'),
]

