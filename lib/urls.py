from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('loginUser', views.loginUser, name='loginUser'),
    path('validate', views.validate, name='validate'),
    path('logout', views.logout_request, name='logout'),
    path('ongoing', views.ongoing, name='ongoing'),
    path('index', views.index, name='index'),
    path('files', views.files, name='files'),
    path('history', views.history, name='history'),
    path('user_reg', views.user_reg, name='user_reg'),
    path('signup', views.signup, name='signup'),
    path('search_book', views.search_book, name='search_book'),
    path('issue', views.issue, name='issue'),
    path('mail', views.mail, name= 'mail'),
    path('search_file', views.search_file, name='search_file'),
    path('issue_file', views.issue_file, name='issue_file'),
    path('renew', views.renew, name='renew'),

]