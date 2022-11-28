from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_service_account = models.BooleanField(
        default=False, verbose_name="Service account?")
    description = models.TextField(max_length=100)

    @property
    def api_routes(self):
        try:
            routes = UserApiRoute.objects.filter(
                user=self)
            return list(routes)
        except Exception as exc:
            return "None"


class ServiceAccount(User):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_service_account = True

    class Meta:
        verbose_name_plural = "Service Accounts"


class Api(models.Model):
    name = models.CharField(max_length=30)

    @property
    def routes(self):
        try:
            routes = ApiRoute.objects.filter(
                api=self)
            return list(routes)
        except:
            return []

    def __str__(self):
        return self.name


class ApiRoute(models.Model):
    api = models.ForeignKey("Api", on_delete=models.CASCADE)
    route = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.route}"


class UserApiRoute(models.Model):
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE)
    api_route = models.ForeignKey("ApiRoute", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.api_route} ({self.user})"
