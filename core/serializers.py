from rest_framework import serializers

from .models import Order, Wallet


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = (
            "url",
            "value",
            "state",
            "currency",
            "created_on",
        )


class WalletSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Wallet
        fields = (
            "url",
            "user",
            "currency",
            "balance",
        )
        read_only_fields = ("user",)
