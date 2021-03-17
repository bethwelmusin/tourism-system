from django.urls import path, include
from . import views
# SET THE NAMESPACE!
# Be careful setting the name to just /login use userlogin instead!
appname = 'recommendation'
urlpatterns=[
    path('index/', views.dashboard, name='index'),
    # path('dashboard/', views.dashboard_view, name='dashboard'),
    path('', views.dashboard, name='index'),
    path('', views.home_view, name='index'),
    path('register/',views.register_view,name='register'),
    path('user_login/',views.user_login,name='loginpage'),
    path("logout/", views.logout_request, name="logout"),
    path("search/", views.search_view, name="search_view"),
]                                                             
