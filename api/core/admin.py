from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from core.models import Api, ApiRoute, User, ServiceAccount, UserApiRoute


class ApiAdmin(admin.ModelAdmin):
    list_display = ["name", "routes"]


class ApiRouteAdmin(admin.ModelAdmin):
    list_display = ["api", "route"]


class UserApiRouteAdmin(admin.ModelAdmin):
    list_display = ["user", "api_route"]


class ServiceAccountAdmin(admin.ModelAdmin):
    list_display = ["username", "description", "api_routes"]


class UserAdmin(BaseUserAdmin):
    list_display = ["username", "is_service_account",
                    "description"]


# Register your models here.
admin.site.unregister(Group)

admin.site.register(Api, ApiAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(ApiRoute, ApiRouteAdmin)
admin.site.register(UserApiRoute, UserApiRouteAdmin)
admin.site.register(ServiceAccount, ServiceAccountAdmin)
