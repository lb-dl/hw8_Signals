from datetime import datetime, timedelta, timezone
from time import sleep
from user.models import Logger


def smth_slow(wait=10):
    sleep(wait)


def old_logs():
    older_than_seven = datetime.now(tz=timezone.utc) - timedelta(days=7)
    Logger.objects.filter(created__lt=older_than_seven).delete
