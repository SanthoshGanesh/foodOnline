from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from accounts.models import User, UserProfile


@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    print(created)
    if created:
        UserProfile.objects.create(user=instance)

    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            # create userprofile if it does not exists
            UserProfile.objects.create(user=instance)


@receiver(pre_save, sender=User)
def pre_save_profile_receiver(instance, sender, **kwargs):
    print(instance.username, "This user is being saved")


# one of way of sending post_save signal to automatically create userprofile after user has been created
# post_save.connect(post_save_create_profile_receiver,sender=User)
