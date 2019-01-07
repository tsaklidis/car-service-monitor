from django.db import models
from django.utils.translation import ugettext_lazy as _


class Car(models.Model):
    brand = models.CharField(max_length=255, blank=False,
                             verbose_name=_(u'Car Brand'), help_text='eg:Fiat')

    def __unicode__(self):
        return u'Company: {0}'.format(self.brand)

    class Meta:
        ordering = ['id']
