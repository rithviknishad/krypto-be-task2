from django.contrib import admin

from .models import Order, Wallet


class OrderAdmin(admin.ModelAdmin):
    model = Order


class WalletAdmin(admin.ModelAdmin):
    model = Wallet


admin.site.register(Order, OrderAdmin)
admin.site.register(Wallet, WalletAdmin)
