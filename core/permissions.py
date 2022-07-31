from rest_framework import permissions


class Order(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return obj.created_by == request.user

        if view.action in ["update", "partial_update"]:
            return False

        if view.action == "destroy":
            return False

        return False

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated

        if view.action == "create":
            return request.user.is_authenticated

        return True


class Wallet(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return obj.user == request.user

        if view.action in ["update", "partial_update"]:
            return False

        if view.action == "destroy":
            return False

        return False

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated

        if view.action == "create":
            return request.user.is_authenticated

        return True
