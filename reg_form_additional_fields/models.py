from django.conf import settings
from django.db import models
from django_countries.fields import CountryField

# Backwards compatible settings.AUTH_USER_MODEL
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class ExtraInfo(models.Model):
    """
    This model contains the extra field "Country" that will be saved when a user registers.
    The form that wraps this model is in the forms.py file.
    """
    user = models.OneToOneField(USER_MODEL, null=True, related_name='user+', on_delete=models.CASCADE)

    country = CountryField()

    def __str__(self):
        result = '{0.user} {0.country}'
        return result.format(self)
