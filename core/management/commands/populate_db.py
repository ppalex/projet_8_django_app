from django.core.management.base import BaseCommand

from .initialize import initialize_job


class Command(BaseCommand):
    """This class contains function to handle arguments.
    """
    help = "Download data from Openfoodfact and populate the db."

    def add_arguments(self, parser):
        parser.add_argument('initialize', type=str, nargs='+',
                            help='Launch the script to create tables in DB, \
                                get data from API and fill DB with data.')

    def handle(self, *args, **options):
        if options['initialize']:
            initialize_job()
