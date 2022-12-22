from django.http import Http404


# Checks if the logged-in user is account owner or staff/superuser before rendering
class AccountPermissionCheckMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj != request.user and not request.user.is_superuser and not request.user.is_staff:
            raise Http404("You are not the owner of this account.")
        return super().dispatch(request, *args, **kwargs)


# Checks if the logged-in user created game or is staff/superuser before rendering
class GamePermissionCheckMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.added_by != request.user and not request.user.is_superuser and not request.user.is_staff:
            raise Http404("You have no permissions to modify this game.")
        return super().dispatch(request, *args, **kwargs)


# Checks if the logged-in user is staff/superuser before rendering
class GenreDevicePermissionCheckMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser and not request.user.is_staff:
            raise Http404("You have no permissions to modify this game.")
        return super().dispatch(request, *args, **kwargs)
