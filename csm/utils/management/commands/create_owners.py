import random
from django.core.management.base import BaseCommand, CommandError

from csm.companies.models import Company
from csm.users.models import Owner
from csm.utils.unique import unique_id


class Command(BaseCommand):
    help = 'Create some fake owners.'

    def add_arguments(self, parser):
        parser.add_argument(
            'total', type=int,
            help='Indicates the number of owners to be created')

        # Optional argument
        # parser.add_argument('-c', '--cars', type=str, help='Create with car', )

    def handle(self, *args, **kwargs):

        total = kwargs['total']
        first_names = ['John', 'Nick', 'George', 'Stahis', 'Bill', 'Kostas']
        last_names = ['Rambo', 'Veggos', 'Vamos', 'Vlachou', 'Kakana']
        genders = [True, False]
        company = Company.objects.last()

        if not total:
            raise CommandError('Erros: How many owners?')

        for i in range(total):
            Owner.objects.create(company=company,
                                 first_name=random.choice(first_names),
                                 last_name=random.choice(last_names),
                                 gender=random.choice(genders),
                                 email=(unique_id() + '@csm.com')
                                 )

        self.stdout.write('Created {0} owners'.format(total))
