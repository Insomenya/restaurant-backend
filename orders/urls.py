from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrderCreateListView.as_view(), name='orders'),
    path('<int:order_id>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('update-status/<int:order_id>', views.UpdateOrderStatusView.as_view(), name='update_order_status'),
    path('user/', views.UserOrdersView.as_view(), name='user_orders'),
    path('user/<int:order_id>/', views.UserSpecificOrder.as_view(), name='user_specific_order')
]