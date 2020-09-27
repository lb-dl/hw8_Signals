# from django.contrib.auth.models import User
from user.models import User

from django.db.models.signals import pre_save
from django.dispatch import receiver


# @receiver(post_save, sender=User)
# def user_post_save(sender, instance, created, **kwargs):


@receiver(pre_save, sender=User)
def user_pre_save(sender, instance, *args, **kwargs):
    correct_phone = ''
    for char in instance.phone:
        if char.isdigit():
            correct_phone += char
    instance.phone = correct_phone
