from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = "Download data from Openfoodfact and populate the db."


    def add_arguments(self, parser):
        parser.add_argument('initialize', type=str, nargs='+',
                        help='Launch the script to create tables in DB, \
                                get data from API and fill DB with data.')

    def handle(self, *args, **options):
        if options['initialize']:
            print('ok')