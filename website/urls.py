from django.urls import path
from .views import home, logout_user

urlpatterns = [
    path('', home, name='home'),
    # path('login/', login_user, name='login'),
    path('logout_user', logout_user, name='logout'),
]