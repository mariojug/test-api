from django.core.management.base import BaseCommand, CommandError

from core.models import Api, ApiRoute, UserApiRoute, User


class Command(BaseCommand):
    help = 'Creates records of permitted api routes for a user/service account'

    def add_arguments(self, parser):
        parser.add_argument('--username', type=str)
        parser.add_argument('--apiname', type=str)
        parser.add_argument('--route', type=str)

    def handle(self, *args, **options):
        api_name = options['apiname']
        route = options['route']
        username = options['username']

        try:
            user = User.objects.get(username=username)
        except:
            raise CommandError(f"User \"{username}\" does not exist")

        try:
            api = Api.objects.get(name=api_name)
        except:
            raise CommandError(f"Api \"{api_name}\" does not exist")

        try:
            api_route = ApiRoute.objects.get(api=api.pk, route=route)
        except:
            raise CommandError(
                F"Api route \"{route}\" does not exist for api \"{api_name}\"")

        user_api_route = UserApiRoute(user=user, api_route=api_route)
        user_api_route.save()
