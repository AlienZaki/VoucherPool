from django.shortcuts import render
from voucher.models import Voucher, Offer
from customer.models import Customer
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.contrib import messages
from datetime import datetime
from .utils import generate_random_string


@login_required(login_url='login')
def home(request):
    if request.user.is_superuser:
        return redirect('vouchers_list')
    else:
        return redirect('vouchers_endpoints')


@login_required(login_url='login')
def vouchers_endpoints(request):
    return render(request, 'vouchers_endpoints.html')


@login_required(login_url='login')
def generate_voucher(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            customer_id = request.POST['customer_id']
            offer_id = request.POST['offer_id']
            expiry_date = request.POST['expiry_date']
            expiry_date = datetime.strptime(expiry_date, '%d %B, %Y').strftime('%Y-%m-%d')
            Voucher.objects.create(customer_id=customer_id, offer_id=offer_id, expire_date=expiry_date, code=generate_random_string(8))
            messages.success(request, 'Voucher has been created successfully!')
            return redirect('vouchers_list')
    else:
        return render(request, 'page-error-401.html', status=401)


@login_required(login_url='login')
def vouchers_list(request):
    if request.user.is_superuser:
        # Search method
        email = request.GET.get('email')
        page_number = request.GET.get('page')
        page_number = page_number if page_number else 1

        vouchers = Voucher.objects.filter(customer__email=email) if email else Voucher.objects.all()
        offers = Offer.objects.all()
        customers = Customer.objects.all()

        # Pagination
        vouchers_paginator = Paginator(vouchers, 10)
        vouchers = vouchers_paginator.get_page(page_number)

        left_index = (int(page_number) - 2)
        if left_index < 1:
            left_index = 1

        right_index = (int(page_number) + 3)
        if right_index > vouchers_paginator.num_pages:
            right_index = vouchers_paginator.num_pages + 1

        custom_range = range(left_index, right_index)

        context = {
            'vouchers': vouchers,
            'offers': offers,
            'customers': customers,
            'custom_range': custom_range,
        }
        return render(request, 'vouchers_list.html', context=context)
    else:
        return render(request, 'page-error-401.html', status=401)








