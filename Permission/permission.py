from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from rest_framework.permissions import BasePermission


class AnyPermissions(BasePermission):

    def get_permissions(self, request):
        """
        Get all of the permissions that are associated with the view.
        """
        content_type = ContentType.objects.get(model='user').id
        model_permission = Permission.objects.filter(content_type=content_type).values_list('id', flat=True)

        user_permission = request.user.groups.all().values_list('permissions', flat=True)
        permission_detail = Permission.objects.filter(id__in=user_permission)

        actual_permission = permission_detail.filter(id__in=model_permission)

        return actual_permission

    def has_permission(self, request, view):
        """
        Check the permissions on the view.
        """
        # if create action is granted to unauthorized user also then.

        if view.action=='create':
            return True

        actual_permission=self.get_permissions(request)



        if actual_permission:
            if view.action=='list':
                if actual_permission.filter(codename='view_user').exists():
                    return True

                return False

            return True

        return False



    def has_object_permission(self, request, view, obj):
        """
        Check the object permissions on the view.
        """
        actual_permission=self.get_permissions(request)


        if actual_permission:
            if view.action=='retrieve':
                if actual_permission.filter(codename='can_retrieve').exists():
                    return True
                return False

            elif view.action == 'update' or view.action=='partial_update':
                if actual_permission.filter(codename='can_change').exists():
                    return True
                return False

            elif view.action == 'destroy':
                if actual_permission.filter(codename='delete_user').exists():
                    return True
                return False

            else:
                return False
