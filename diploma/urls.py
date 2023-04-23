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

    path('politika_prog/', views.politika, name='politika'),
    path('organ_i_rektor/', views.organ_i_rek, name='organ'),
    path('uchebnyi_process/', views.uchebnyi_proces, name='uchebnyi'),
    path('nauchno_/', views.nauchno, name='nauchno'),
    path('vospit_rabot/', views.vospitatel, name='vospitatel'),
    path('mezhdunarodnoe_/', views.mezhdunarod, name='mezhdunarod'),
    path('personal_manage/', views.personal, name="personal"),
    path('admin_hozyai/', views.admin_hozyai, name='admin_hoz'),

    path('history/', views.history, name='history'),

    path('category/<str:cat_s>/', views.categories, name='category'),
    path('results/', views.results, name='results'),
    path('update_files/<int:id>', views.update_file, name='update'),
    path('view_file/', views.read_file, name='view_file'),
]

