from django.urls import path
from .views import home, logout_user, register_user, customer_record, delete_customer, add_record, update_record

urlpatterns = [
    path('', home, name='home'),
    # path('login/', login_user, name='login'),
    path('logout_user', logout_user, name='logout'),
    path('register', register_user, name='register'),
    path('records/<int:pk>', customer_record, name='record'),
    path('delete_record/<int:pk>', delete_customer, name='delete'),
    path('add_record', add_record, name='add_record'),
    path('update_record/<int:pk>', update_record, name='update_record'),
]