from rest_framework import permissions

from .models import Teacher


class IsOwnerOrReadOnly(permissions.BasePermission):
    message = 'Is Not Owner.'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS \
                or request.user.is_superuser:
            return True
        return request.user == obj.owner


class IsTeacherOrCannotCreate(permissions.BasePermission):
    message = 'Teacher can create classes'

    def has_permission(self, request, view):
        if request.method == 'POST':
            return Teacher.objects.filter(user_id=request.user.id).exists() or request.user.is_superuser
        return True
