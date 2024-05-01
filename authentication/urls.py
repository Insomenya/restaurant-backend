from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.UserCreateView.as_view(), name='sign_up'),
    path('details/', views.UserDetailsView.as_view(), name='user_details')
]