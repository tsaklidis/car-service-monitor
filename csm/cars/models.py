from django.db import models
from django.utils.translation import ugettext_lazy as _

MOVE_CHOICES = (
    (None, '4X4'),
    (True, 'FWD'),
    (False, 'BCK'),
)

GEARS = (
    (True, 'Manual'),
    (False, 'Auto'),
)


class Car(models.Model):
    company = models.ForeignKey('companies.Company')

    owner = models.ForeignKey(
        'users.Owner', related_name='owner', blank=True, null=True)

    brand = models.CharField(max_length=255, blank=False,
                             verbose_name=_(u'Car Brand'), help_text='eg:Fiat')

    kilometers = models.IntegerField(blank=False, null=False)

    price = models.IntegerField(blank=False, null=False)

    hp = models.IntegerField(blank=False, null=False, verbose_name=_(u'HP'))

    cc = models.IntegerField(blank=False, null=False)

    # auto = True
    # manual = False
    gearbox = models.NullBooleanField(default=False, blank=False,
                                      null=False, choices=GEARS,
                                      verbose_name=_(u'Gear box type'))

    color = models.CharField(max_length=255, blank=False,
                             verbose_name=_(u'Color'), help_text='eg:red')

    euro_type = models.CharField(max_length=10, blank=True, null=True,
                                 verbose_name=_(u'Euro type'),
                                 help_text='eg:euro 5')

    license_plate = models.CharField(max_length=10, blank=True, null=True,
                                     verbose_name=_(u'license'),
                                     help_text='eg:KZP1234')

    serial = models.CharField(
        help_text="Car's serial number",
        max_length=255,
        blank=True, null=True)

    fuel = models.CharField(max_length=20, blank=False,
                            verbose_name=_(u'Car fuel'), help_text='eg:Gas')

    owners_before = models.IntegerField(
        blank=False, null=False, help_text='How many owners before you?')

    movement = models.NullBooleanField(default=True, blank=False, null=False,
                                       choices=MOVE_CHOICES)

    manufactured = models.DateTimeField(blank=False, null=False)

    airbags = models.IntegerField(blank=False, null=False,
                                  help_text='If no airbag type 0')

    garage = models.ForeignKey('companies.Garage', blank=True, null=True)

    dors = models.IntegerField(blank=False, null=False)

    created_on = models.DateTimeField(auto_now_add=True)

    # TODO
    # On car create add owner and car to history
    # Use signals

    def __unicode__(self):
        return u'Brand: {0}'.format(self.brand)

    class Meta:
        ordering = ['id']


class CarOwnerHistory(models.Model):
    owner = models.ForeignKey('users.Owner')

    car = models.ForeignKey(Car)

    company = models.ForeignKey('companies.Company')

    def __unicode__(self):
        return u'Owner: {0} Car:'.format(self.owner, self.car)
