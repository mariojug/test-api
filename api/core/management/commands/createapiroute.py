from django.core.management.base import BaseCommand, CommandParser
from core.models import Api, ApiRoute


class Command(BaseCommand):
    help = 'Creates a new Api model and its ApiRoute models'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('--apiname', type=str)
        parser.add_argument('--routes', nargs="+", type=str)

    def handle(self, *args, **options):
        api_name = options['apiname']

        # check if an api model exists with this name
        try:
            api = Api.objects.get(name=api_name)
        except Exception as exc:
            api = Api(name=api_name)
            api.save()

        # check if the route(s) specified for the api exist
        for route in options['routes']:
            try:
                api_route = ApiRoute.objects.get(api=api, route=route)
            except Exception as exc:
                api_route = ApiRoute(api=api, route=route)
                api_route.save()
