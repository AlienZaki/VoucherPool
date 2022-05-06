from django.urls import path
from . import views
from . import api

urlpatterns = [
    path('vouchers/all/', views.vouchers_list, name='vouchers_list'),
    path('vouchers/endpoints/', views.vouchers_endpoints, name='vouchers_endpoints'),
    path('home/', views.home, name='home'),

    # Endpoints
    path('api/vouchers/', api.customer_vouchers, name='customer_vouchers'),
    path('api/voucher/redeem/', api.redeem_voucher, name='redeem_voucher'),

]