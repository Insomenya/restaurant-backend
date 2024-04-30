from django.urls import path
from . import views

urlpatterns = [
    path('', views.AuthView.as_view(), name='auth'),
    path('signup/', views.UserCreateView.as_view(), name='sign_up'),
    path('details/', views.UserDetailsView.as_view(), name='sign_up')
]