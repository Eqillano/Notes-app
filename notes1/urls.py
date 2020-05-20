from django.urls import path,include
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,CategoryCreateView,CategoryListView,FavouriteView,FavouriteList
#from . import views

urlpatterns = [
   path('',PostListView.as_view(),name='blog-home'),
   path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
   path('post/new/',PostCreateView.as_view(),name='post-create'),
   path('category/new/',CategoryCreateView.as_view(),name='category-create'),
   path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
   path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
   #path('category/<str:cats>/',CategoryView,name='category'),
   path('category-list/',CategoryListView,name='category-list'),
   path('fav/<int:pk>/',FavouriteView,name='fav-post'),
   path('fav_list/',FavouriteList,name='fav_list'),
  # path('about/',views.about,name='blog-about'),
]
