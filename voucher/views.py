from django.shortcuts import render
from voucher.models import Voucher, Offer
from customer.models import Customer
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.core.paginator import Paginator


@login_required(login_url='login')
def vouchers_list(request):
    if request.user.is_superuser:
        page_number = request.GET.get('page')
        page_number = page_number if page_number else 1

        vouchers = Voucher.objects.all()
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


@login_required(login_url='login')
def vouchers_endpoints(request):
    return render(request, 'vouchers_endpoints.html')


@login_required(login_url='login')
def home(request):
    if request.user.is_superuser:
        return redirect('vouchers_list')
    else:
        return redirect('vouchers_endpoints')


