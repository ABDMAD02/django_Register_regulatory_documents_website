from django.urls import path 
from . import views # dot . it's mean 'current package' 

urlpatterns = [
    path('', views.welcome, name="home"),
    path('pattern/', views.pat, name="pattern"),
    path('login/', views.logPage, name="login"),
    path('logout/', views.LogOut, name="logout"),
    path('registration/', views.reg, name="registration"),
    path('profile/', views.profile, name='profile'),
    path('account_settings/', views.acc_settings, name='account_settings'),
    path('upload_files/', views.file_up, name='uploadfile'),
    path('delete_file/<int:pk>', views.delete_file, name='delete_file'),
    path('politika_prog/', views.politika, name='politika'),
    path('organ_i_rektor/', views.organ_i_rek, name='organ'),
    path('recomendacii/', views.suggestion, name='recomendacii'),
    path('pravila/', views.pravilaa, name='pravila'),
    path('procedury/', views.procedura, name='procedura'),
    path('VND/', views.vnutrii, name='vnd'),
]

