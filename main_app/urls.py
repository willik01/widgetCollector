from django.urls import path
from . import views
# from main_app.views import WidgetList

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

      # route for widget index
    path('widgets/', views.widgets_index, name='index'),
    # path('widgets/', views.WidgetList.as_view(), name='index'), #WTF?
    
    path('widgets/<int:widget_id>/', views.widgets_detail, name='detail'),
    path('widgets/create/', views.WidgetCreate.as_view(), name='widget_create'),
    path('widgets/<int:pk>/update/', views.WidgetUpdate.as_view(), name='widgets_update'),
    path('widgets/<int:pk>/delete/', views.WidgetDelete.as_view(), name='widgets_delete'),
]
