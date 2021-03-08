from django.core.exceptions import ImproperlyConfigured
from django.conf import settings


def get_setting(name):
    try:
        return getattr(settings, name)
    except AttributeError:
        raise ImproperlyConfigured(f"You Haven't Configured Your UpStorage Settings Properly. Missing '{name}'")
