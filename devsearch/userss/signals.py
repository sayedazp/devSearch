from django.db.models import signals
from django.dispatch import receiver
from .models import User, Profile

@receiver(signals.post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name
        )
@receiver(signals.post_delete, sender=Profile)
def deleteProfile(sender, instance, **kwargs):
    user = instance.user
    user.delete()
