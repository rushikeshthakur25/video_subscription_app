from django.urls import path,include
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index,name='index'),
    path('upmovie/',views.upmovie,name='up'),
    path('list/',views.list,name='list'),
    path('login/',auth_views.LoginView.as_view(template_name='sub/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('signup/',views.signup,name='signup'),
    path('price/',views.price,name='price'),
    path('display_movie/',views.display_movie,name='display_movie'),
    path('price/plans/', views.price, name='price-plans'),
    path('subscription/subscribe/<int:plan_id>/', views.subscribe, name='subscribe'),
    # path('profile/', views.profile, name='user-profile'),

]

