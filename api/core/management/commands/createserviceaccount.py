from django.core.management.base import BaseCommand, CommandError, CommandParser
from core.models import ServiceAccount


class Command(BaseCommand):
    help = 'Creates a new service account object and attaches permitted routes'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('--username', nargs=1, type=str)
        parser.add_argument('--password', nargs=1, type=str)
        parser.add_argument('--description', type=str)

    def handle(self, *args, **options):
        print(options['description'])
        service_account = ServiceAccount(username=options['username'][0])
        service_account.set_password(options['password'][0])
        # service_account.is_service_account = True
        service_account.description = options["description"]
        service_account.save()
