from django.urls import path
from . import views
from .views import CustomLoginView, CustomLogoutView, RegisterView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', CustomLoginView.as_view(template_name='auth-login-basic.html'), name='login'),
    path('kepuasan_umum/', views.kuesioner, name='kuesioner'),
    path('tingkat_kepentingan/', views.kuesioner1, name='kuesioner1'),
    path('tingkat_kepuasan/', views.kuesioner2, name='kuesioner2'),
    path('index/', views.index, name='index'),
    path('register/', RegisterView.as_view(), name='register'),
    path('forgotpass/', views.forgotpass, name='forgotpass'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('registersuccess/', views.registerSuccess, name='registersuccess'),
    path('profile/', views.accountprofile, name='profile'),
    path('quesionaire/', views.quesionaire, name='quesionaire'),
    path('login/', auth_views.LoginView.as_view(template_name='auth-login-basic.html'), name='auth_login'),
    path('thank_you/', views.thank_you, name='thank_you'),
    path('thank_you1/', views.thank_you1, name='thank_you1'),
    path('thank_you2/', views.thank_you2, name='thank_you2'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('adminlogin/', views.admin_login, name='admin_login'),
    path('adminlogout/', views.admin_logout, name='admin_logout'),
    path('dashboard/participant_list', views.participant_list, name='participant_list'),
    path('dashboard/add_participant/', views.add_participant, name='add_participant'),
    path('dashboard/delete_user/', views.delete_user, name='delete_user'),
    path('edit-user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('user-count/', views.count_user_umums, name='user_count'),
    path('sum-kepentingan/', views.sum_dimensi_kepentingan, name='dimensi_kepentingan'),
    path('sum-kepuasan/', views.sum_dimensi_kepuasan, name='dimensi_kepuasan'),
    path('dashboard/jabatan_list/', views.jabatan_list, name='jabatan_list'),
    path('dashboard/index/', views.dashboard2, name='dashboard2'),
    path('dashboard/komentar-saran/', views.dashboard3, name='dashboard3'),
    path('chart_view/', views.position_chart, name='chart_view'),
    path('update_chart/', views.update_chart, name='update_chart'),
    path('dashboard/manage_kuesioner', views.manage_kuesioner, name='manage_kuesioner'),
    path('dashboard/add_kuesioner', views.add_kuesioner, name='add_kuesioner'),
    path('manage_kuesioner/edit_umum/<int:id>/', views.edit_kepuasan_umum, name='edit_kepuasan_umum'),
    path('manage_kuesioner/edit_kepentingan/<int:id>/', views.edit_kepentingan, name='edit_kepentingan'),
    path('manage_kuesioner/edit_kepuasan/<int:id>/', views.edit_kepuasan, name='edit_kepuasan'),
    path('count-lvl-kepentingans/', views.score_sum_kepentingans, name='score_sum_kepentingan'),
    path('count-lvl-kepuasans/', views.score_sum_kepuasans, name='score_sum_kepuasan'),
    path('scores/', views.display_scores, name='scores'),
    path('count-kepuasan/', views.count_user_kepuasans, name= 'count_user_kepuasan'),
    path('lvl_scores/', views.lvl_scores, name= 'lvl_scores'),
    path('user_comment/', views.user_comment, name='user_comment')
]
    