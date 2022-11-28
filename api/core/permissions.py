from django.urls import resolve
from django.db.models import Q
from rest_framework.permissions import BasePermission, SAFE_METHODS

from core import models


class CorePermission(BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False

        resolver_match = resolve(request.path_info)

        user = models.User.objects.get(pk=request.user.pk)
        api = models.Api.objects.filter(
            name=resolver_match.app_name).first()

        api_route = models.ApiRoute.objects.filter(
            api=api, route=resolver_match.route)
        if api_route:
            api_route = api_route[0]

        try:
            user_api_route = models.UserApiRoute.objects.filter(
                user=user, api_route=api_route.pk).first()
        except:
            return False
        else:
            return True
