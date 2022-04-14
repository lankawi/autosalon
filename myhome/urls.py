from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:auto_id>', views.show_auto, name='show_auto'),
    #path('home/', views.posts, name='posts'),
]