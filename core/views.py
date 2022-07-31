from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

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
