# import string
from user.utils import old_logs, smth_slow

from celery import shared_task

from django.core.mail import send_mail
# from django.contrib.auth.models import User
# from django.utils.crypto import get_random_string


@shared_task
def smth_slow_async(wait=10):
    # print('1'*100)
    smth_slow(wait)


@shared_task
def send_email_async(subject, text):
    send_mail(
        subject,
        text,
        'lbdltest77@gmail.com',
        ['sensitivestory@gmail.com'],
        fail_silently=False,
    )


@shared_task
def old_logs_async():
    old_logs()
