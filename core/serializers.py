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
            "created_by",
        )
        read_only_fields = ("created_by",)


class WalletSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Wallet
        fields = (
            "url",
            "user",
            "currency",
            "balance",
        )
        read_only_fields = (
            "user",
            "balance",
        )
