from rest_framework_api_key.permissions import HasAPIKey


class HasAPIKeyPermission(HasAPIKey):
    def has_permission(self, request, view):
        return self.has_key(request)