from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('post/<str:pk>',views.post, name="post"),
    path('form_post/', views.formulario, name="formPost"),
    path('delete-post/<str:pk>/', views.deletePost, name="delete-post"),    
    path('update-post/<str:pk>/', views.updatePost, name="update-post")

    
]
