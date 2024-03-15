from django.urls import path
from finanser.views.views_auth import RegisterView, LoginView, LogoutView

urlpatterns = [
  path('register/', RegisterView.as_view(), name='register'),
  path('login/', LoginView.as_view(), name='login'),
  path('logout/', LogoutView.as_view(), name='logout'),
]
