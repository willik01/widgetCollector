from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
      # route for widget index
    path('widgets/', views.widgets_index, name='index'),
]
