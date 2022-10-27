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
    path('widgets/<int:widget_id>/add_cleaning/', views.add_cleaning, name='add_cleaning'),

    path('accessories/', views.AccessoryList.as_view(), name='accessories_index'),
    path('accessories/<int:pk>/', views.AccessoryDetail.as_view(), name='accessories_detail'),
    path('accessories/create/', views.AccessoryCreate.as_view(), name='accessories_create'),
    path('accessories/<int:pk>/update/', views.AccessoryUpdate.as_view(), name='accessories_update'),
    path('accessories/<int:pk>/delete/', views.AccessoryDelete.as_view(), name='accessories_delete'),
    path('accessories/<int:widget_id>/assoc_accessory/<int:accessory_id>/', views.assoc_accessory, name='assoc_accessory'),
]
