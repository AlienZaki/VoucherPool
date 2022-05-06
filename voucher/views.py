from django.shortcuts import render
from voucher.models import Voucher
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def vouchers_list(request):
    context = {
        'vouchers': Voucher.objects.all(),
    }
    return render(request, 'vouchers_list.html', context=context)



