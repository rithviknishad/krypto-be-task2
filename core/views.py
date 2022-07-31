from decimal import Decimal
from django.http import HttpResponseRedirect
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from . import permissions
from .models import Order, Wallet
from .serializers import OrderSerializer, WalletSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (
        IsAuthenticated,
        permissions.Order,
    )

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)

    def get_wallet(self, currency=None) -> Wallet:
        currency = currency or self.request.data.get("currency")
        try:
            wallet: Wallet = Wallet.objects.get(user=self.request.user, currency=currency)
        except Wallet.DoesNotExist:
            raise Exception(f"No wallet for currency '{currency}'")
        return wallet

    def create(self, request, *args, **kwargs):
        self.get_wallet().debit(Decimal(request.data.get("value")))
        return super().create(request, *args, **kwargs)

    @action(detail=True, url_path="cancel", methods=["get"])
    def cancel(self, request, *args, **kwargs):
        instance: Order = self.get_object()
        self.get_wallet(currency=instance.currency).credit(instance.value)
        instance.state = Order.STATE_CANCEL
        instance.save(update_fields=["state"])
        return HttpResponseRedirect("../")


class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    permission_classes = (
        IsAuthenticated,
        permissions.Wallet,
    )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    # TODO: make it POST instead
    @action(detail=True, url_path="credit", methods=["get"])
    def credit(self, request, *args, **kwargs):
        # TODO: history of credit and debit transactions with timestamp
        amount = Decimal(self.request.query_params.get("amount"))
        self.get_object().credit(amount)
        return HttpResponseRedirect("../")

    @action(detail=True, url_path="debit", methods=["get"])
    def debit(self, request, *args, **kwargs):
        # TODO: history of credit and debit transactions with timestamp
        amount = Decimal(self.request.query_params.get("amount"))
        self.get_object().debit(amount)
        return HttpResponseRedirect("../")
