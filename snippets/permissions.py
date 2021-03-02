from rest_framework import permissions


class ISOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        # so we'll always allow GET, HEAD or OPTIONS requests
        if request.method is permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


