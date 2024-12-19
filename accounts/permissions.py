from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    """
    Custom permission to grant access only to users with the 'admin' role and who are authenticated.
    """

    def has_permission(self, request,view):
        return request.user.is_authenticated and request.user.role == 'Admin'
    
class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only admins for unsafe methods (POST, PUT, DELETE).
    Safe methods (GET, HEAD, OPTIONS) are allowed for everyone.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return (
            request.user.is_authenticated 
            and (getattr(request.user, 'role', None) == 'Admin' or request.user.is_staff)
        )
    
