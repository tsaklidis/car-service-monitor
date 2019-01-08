from django.db import models
from django.utils.translation import ugettext_lazy as _

from csm.utils.unique import unique_id


GENDER_CHOICES = (
    (None, 'Gender'),
    (True, 'Female'),
    (False, 'Male'),
)


class Owner(models.Model):
    company = models.ForeignKey('companies.Company', related_name='owners')

    first_name = models.CharField(max_length=255, default='',
                                  blank=False, null=False,
                                  verbose_name=_(u'First Name'))

    middle_name = models.CharField(max_length=255, default='',
                                   blank=True, null=True,
                                   verbose_name=_(u'Middle Name'))

    last_name = models.CharField(max_length=255, default='',
                                 blank=False, null=False,
                                 verbose_name=_(u'Last Name'))

    gender = models.NullBooleanField(default=None, blank=True, null=True,
                                     choices=GENDER_CHOICES,
                                     verbose_name=_(u'Gender'))

    birth_date = models.DateField(blank=True, null=True,
                                  help_text="Owner's birth date")

    created_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    email = models.EmailField(blank=False, null=False,
                              help_text="Owner's email")
    serial = models.CharField(
        help_text="Owner's serial number",
        max_length=100,
        blank=True, null=True,
        default=unique_id)

    def full_name(self):
        """Returns the first_name, middle_name plus the last_name,
        with a space in between.
        """
        if self.middle_name:
            full_name = _(u'{0} {1} {2}').format(self.first_name,
                                                 self.middle_name,
                                                 self.last_name)
        else:
            full_name = _(u'{0} {1}').format(self.first_name,
                                             self.last_name)

        if not self.first_name and not self.last_name:
            return 'N/A'
        else:
            return full_name

    def __unicode__(self):
        return u'{0} {1}'.format(self.first_name, self.last_name)
