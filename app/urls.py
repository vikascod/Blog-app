from django.urls import path
from app import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('blog/<int:pk>/', views.IndexDetailView.as_view(), name='detail'),
    path('add-post', views.AddPostView.as_view(), name='add_post'),
    path('blog/edit/<int:pk>/', views.UpdatePostView.as_view(), name='update_post'),
    path('delete/<int:pk>/', views.DeletePostView.as_view(), name='delete_post'),
    path('category/<str:cats>/', views.categoryView, name='category'),
    path('like/<int:pk>/', views.likeView, name='like_post'),
    path('blog/<int:pk>/comment/', views.AddCommentView.as_view(), name='comment'),
    path('search/', views.search, name='search')
]