from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='myapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('debug-template/', views.debug_template),
    path('search/', views.search, name='search'),


    # Forum views
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:category_id>/new/', views.create_thread, name='create_thread'),
    path('categories/<int:category_id>/', views.thread_list, name='thread_list'), 
    path('threads/<int:thread_id>/', views.thread_detail, name='thread_detail'),
    path('posts/<int:post_id>/reply/', views.reply_post, name='reply_post'),
    path('posts/<int:post_id>/upvote/', views.upvote_post, name='upvote_post'),
    path('posts/<int:post_id>/downvote/', views.downvote_post, name='downvote_post'),
    path('posts/<int:post_id>/report/', views.report_post, name='report_post'),
]