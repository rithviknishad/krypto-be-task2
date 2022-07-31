from decimal import Decimal

from django.db import models


class Order(models.Model):
    STATE_CANCEL = "cancel"
    STATE_PENDING = "pending"
    STATE_SUCCESS = "success"
    STATE_CHOICES = [
        (STATE_CANCEL, "Cancel"),
        (STATE_PENDING, "Pending"),
        (STATE_SUCCESS, "Success"),
    ]

    created_by = models.ForeignKey(
        "users.User",
        related_name="orders",
        null=False,
        on_delete=models.CASCADE,
    )
    created_on = models.DateTimeField(
        blank=False,
        null=False,
        auto_now_add=True,
    )
    currency = models.CharField(
        max_length=255,
        blank=False,
    )
    state = models.CharField(
        max_length=255,
        blank=False,
        choices=STATE_CHOICES,
        default=STATE_PENDING,
    )
    value = models.DecimalField(
        max_digits=64,
        decimal_places=32,
        blank=False,
        null=False,
    )


class Wallet(models.Model):
    balance = models.DecimalField(
        max_digits=64,
        decimal_places=32,
        blank=False,
        null=False,
        default=Decimal("0"),
    )
    currency = models.CharField(
        max_length=255,
        blank=False,
    )
    user = models.ForeignKey(
        "users.User",
        related_name="wallets",
        null=False,
        on_delete=models.CASCADE,
    )
