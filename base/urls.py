from django.urls import path
from . import views
from .views import PostDetailView, PostEditView, PostDeleteView, CommentDeleteView, AddLike, AddDislike



urlpatterns = [
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('register', views.registerPage, name='register'),
    path('', views.home, name='home'),
    path('profile/<str:pk>', views.friendspage, name='profile'),
    path('profile/<str:pk>/edit', views.editprofile, name='edit'),
    
    path('uploadpost', views.postPost, name='uploadpost'),
    path('post/<int:pk>', PostDetailView.as_view(), name = 'post-detail'),
    path('post/edit/<int:pk>/', PostEditView.as_view(), name='post-edit'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name = 'post-delete'),
    path('post/<int:post_pk>/comment/delete/<int:pk>/', CommentDeleteView.as_view(), name = 'comment-delete'),
    path('post/<int:pk>/like', AddLike.as_view(), name='like'),
    path('post/<int:pk>/dislike', AddDislike.as_view(), name='dislike'),
]