from .models import Voucher
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import VoucherSerializer
from datetime import date


@api_view(['GET'])
def customer_vouchers(request):
    vouchers = Voucher.objects.filter(customer__email=request.GET['email'], is_used=False, expire_date__gte=date.today())
    data = VoucherSerializer(vouchers, many=True).data
    res = {
        'data': data,
    }
    return Response(res)


@api_view(['GET', 'POST'])
def redeem_voucher(request):
    code = request.GET['code']
    email = request.GET['email']
    res = {}
    try:
        # In Case it is valid, return the Percentage Discount
        voucher = Voucher.objects.get(customer__email=email, code=code)
        if voucher.is_used or voucher.used_date:
            res['success'] = False
            res['msg'] = 'This voucher has been redeemed before'
        elif voucher.is_expired:
            res['success'] = False
            res['msg'] = 'This voucher has been expired'
        else:
            # Valid Code, redeem it.
            res['success'] = True
            res['data'] = {
                    'discount_percentage': voucher.offer.discount_percentage
            }
            # Set the date of usage
            voucher.used_date = date.today()
            voucher.is_used = True
            voucher.save()
    except Voucher.DoesNotExist:
        res['success'] = False
        res['msg'] = 'Invalid voucher code!'

    return Response(res)