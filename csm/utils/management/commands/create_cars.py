import random
# import datetime
from django.utils import timezone
import pytz
from django.core.management.base import BaseCommand, CommandError

from csm.cars.models import Car
from csm.users.models import Owner
from csm.utils.unique import unique_id


class Command(BaseCommand):
    help = 'Create some fake cars.'

    def add_arguments(self, parser):
        parser.add_argument(
            'total', type=int,
            help='Indicates the number of cars to be created')

    def handle(self, *args, **kwargs):

        GEARS = MOVE_CHOICES = [True, False, None]

        total = kwargs['total']
        brands = ['Fiat', 'Citroen', 'Toyota', 'Rover', 'Alfa Romeo', 'Opel']
        colors = ['Red', 'Blue', 'Black', 'Silver', 'White', 'Yellow', 'Pink']
        plate = ['KZP', 'NHM', 'KBP', 'TPK', 'MNA']

        if not total:
            raise CommandError('Erros: How many cars?')

        for i in range(total):

            # Random '?' Will kill the db server
            # on the second day in production

            owner = Owner.objects.order_by('?').first()
            Car.objects.create(owner=owner,
                               brand=random.choice(brands),
                               company=owner.company,
                               kilometers=random.randint(10000, 200000),
                               price=random.randint(2000, 20000),
                               hp=random.randint(50, 200),
                               cc=random.randint(800, 3000),
                               gearbox=random.choice(GEARS),
                               color=random.choice(colors),
                               euro_type='euro' + str(random.randint(1, 5)),
                               license_plate=random.choice(
                                   plate) + str(random.randint(1000, 9999)),
                               serial=unique_id(10),
                               fuel='GAS',
                               owners_before=random.randint(0, 10),
                               movement=random.choice(MOVE_CHOICES),
                               manufactured=timezone.now(),
                               airbags=random.randint(0, 6),
                               dors=random.randint(2, 6)
                               )

        self.stdout.write('Created {0} cars'.format(total))
