from django.db.models.signals import post_save 
from django.dispatch import receiver
from ..models import Certs
from .tasks import refresh_certs_messages_to_db


@receiver(post_save, sender=Certs)
def certs_pre_create_or_update(sender, instance, **kwargs):
    refresh_certs_messages_to_db(instance.id)
    return instance
