from django.urls import path 
from . import views # dot . it's mean 'current package' 

urlpatterns = [
    path('', views.welcome, name="home"),
    path('login/', views.logPage, name="login"),
    path('logout/', views.LogOut, name="logout"),
    path('registration/', views.reg, name="registration"),
    path('profile/', views.profile, name='profile'),
    path('account_settings/', views.acc_settings, name='account_settings'),

    path('upload_files/', views.file_up, name='uploadfile'),
    path('delete_file/<int:pk>', views.delete_file, name='delete_file'),

    path('history/', views.history, name='history'),
 
    path('category/<str:cat_s>/', views.categories, name='category'),

    path('results/', views.results, name='results'),
    path('update_files/<int:id>', views.update_file, name='update'),
    # path('view_file/', views.read_file, name='view_file'),
]

