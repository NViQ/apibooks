from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Пользователь может только просматривать, но не редактировать книги, если он не является их автором
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user
