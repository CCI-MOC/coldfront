import os

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand

base_dir = settings.BASE_DIR


class Command(BaseCommand):

    def handle(self, *args, **options):
        call_command('migrate')
        call_command('import_field_of_science_data')
        call_command('add_default_grant_options')
        call_command('add_default_project_choices')
        call_command('add_default_subscription_choices')
        call_command('add_default_publication_sources')
