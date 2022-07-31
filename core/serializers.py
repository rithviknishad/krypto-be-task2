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
        read_only_fields = ("state",)


class WalletSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Wallet
        fields = (
            "url",
            "currency",
            "balance",
        )
        read_only_fields = (
            "user",
            "balance",
        )
