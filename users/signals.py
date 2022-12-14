from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# khi user duoc create thi profile cua ng do cung se dc create
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        print("tao profile")
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, *args, **kwargs):
    print("save profile")
    instance.profile.save()


@receiver(post_delete, sender=Profile)
def auto_delete_user_with_profile(sender, instance, *args, **kwargs):
    instance.user.delete()
