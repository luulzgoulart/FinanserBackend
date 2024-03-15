from django.urls import path
from finanser.views.views_auth import LoginView, LogoutView

urlpatterns = [
  path('login/', LoginView.as_view(), name='login'),
  path('logout/', LogoutView.as_view(), name='logout'),
]
