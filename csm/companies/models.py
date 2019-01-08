import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from uuslug import uuslug as slugify


class Company(models.Model):

    manager = models.OneToOneField(User)

    name = models.CharField(max_length=255, blank=False,
                            verbose_name=_(u'Name'))
    slug = models.SlugField(unique=True, blank=True, max_length=255)

    website = models.URLField(verbose_name=_(u'Website'),
                              help_text=_(u'Company website'))
    founded = models.DateField(
        default=datetime.date.today, verbose_name=_(u'Founded'),
        blank=True, null=True, help_text=_(u'When was company founded'))

    address = models.CharField(max_length=60, blank=True, null=True,
                               help_text=_(u'Address'))
    city = models.CharField(max_length=60, blank=True, null=True,
                            help_text=_(u'City'))

    company_size = models.IntegerField(
        default=0,
        verbose_name=_(u'Company Size'),
        help_text=_(u'How many employees does company have'))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, instance=self)
        super(Company, self).save(*args, **kwargs)

    def __unicode__(self):  # __str__() for python 3
        return u'Company: {0}'.format(self.name)

    class Meta:
        verbose_name_plural = _('companies')
        ordering = ['id']


class Department(models.Model):

    name = models.CharField(
        max_length=100, blank=False, null=False, verbose_name=_(u'Name'),
        help_text=_(u'Please give a name to company\'s department'))
    slug = models.SlugField(unique=True, blank=True,
                            max_length=200)

    company = models.ForeignKey(Company, related_name='departments')

    def employees_count(self):
        pass

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(
                u'{0}-{1}'.format(self.company.name, self.name),
                instance=self)
        super(Department, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'Department: {0}'.format(self.name)

    class Meta:
        unique_together = ('company', 'name')
