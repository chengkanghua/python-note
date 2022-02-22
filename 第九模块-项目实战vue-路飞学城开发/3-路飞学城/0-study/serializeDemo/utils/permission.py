from rest_framework.permissions import BasePermission

# http://127.0.0.1:8000/auth/test?token=160b85f738ca4869bc9ac2ec41e07709
class MyPermission(BasePermission):
    message = "您没有权限"

    def has_permission(self, request, view):
        user_obj = request.user
        if user_obj.type == 3:
            return False
        else:
            return True
