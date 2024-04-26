from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrderListView.as_view(), name='orders'),
    path('create/', views.OrderCreationView.as_view(), name='place_order'),
    path('admin/<int:order_id>/', views.AdminSpecificOrderView.as_view(), name='admin_specific_order'),
    path('admin/update-status/<int:order_id>/', views.UpdateOrderStatusView.as_view(), name='admin_update_order_status'),
    path('cancell/<int:order_id>/', views.CancellOrderView.as_view(), name='user_cancell_order'),
    path('<int:order_id>/', views.UserSpecificOrderView.as_view(), name='user_specific_order')
]