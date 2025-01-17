from django.core.exceptions import PermissionDenied


class UserIsOwnerMixin(object):
    def dispatch(self, request, *args, **kwargs):
        instance = self.get_object()
        print(instance)
        if instance.creator != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)