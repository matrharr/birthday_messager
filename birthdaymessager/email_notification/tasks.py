from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

from birthdaymessager.utils import bday_email

logger = get_task_logger(__name__)

@periodic_task(
  run_every=(crontab(minute='*15')),
  name="task_bday_email",
  ignore_result=True
  )
def task_bday_email():
  bday_email()
  logger.info("Saved image from Flickr")