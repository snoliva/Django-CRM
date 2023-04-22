from django.urls import path
from .views import home, logout_user, register_user, customer_record, delete_customer

urlpatterns = [
    path('', home, name='home'),
    # path('login/', login_user, name='login'),
    path('logout_user', logout_user, name='logout'),
    path('register', register_user, name='register'),
    path('records/<int:pk>', customer_record, name='record'),
    path('delete_record/<int:pk>', delete_customer, name='delete'),
]