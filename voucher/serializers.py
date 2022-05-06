from django.contrib.auth.models import User
from rest_framework import serializers
from voucher.models import Voucher, Offer


class VoucherSerializer(serializers.ModelSerializer):
    offer = serializers.StringRelatedField()

    class Meta:
        model = Voucher
        fields = ['code', 'offer', 'expire_date']




