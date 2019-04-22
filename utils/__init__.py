import hashlib

from django.utils import timezone


def hash256(value):
    return hashlib.sha256(value.encode()).hexdigest()


def local_date(instance=None):
    if not instance:
        instance = timezone.now()

    return timezone.localdate(instance)