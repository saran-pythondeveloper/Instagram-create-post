from django.urls import path
from . import views

urlpatterns = [
    path('',views.signupPage, name='signupPage'),
    path('login/', views.loginPage, name='loginPage'),
    path('home/',views.homePage, name='homePage'),
    path('logout/',views.logoutUser, name='logout'),
    path('create/', views.createPostPage, name='createPostPage'),
    path('like/<int:post_id>/', views.likePost, name='likePost'),
    path('comment/<int:post_id>/', views.commentPost, name='commentPost'),
]
