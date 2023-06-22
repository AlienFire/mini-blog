from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostView.as_view()), 
    path('<int:pk>/add_likes/', views.AddLike.as_view(), name='add_likes'),
    path('<int:pk>/del_likes/', views.DelLike.as_view(), name='del_likes'),
    path('<int:pk>/', views.PostDetall.as_view()),
    path('review/<int:pk>/', views.AddComments.as_view(), name='add_comments'),

]