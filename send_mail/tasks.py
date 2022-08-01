from django.contrib.auth import get_user_model

from celery import shared_task
from django.core.mail import send_mail
from django_celery import settings
from django.utils import timezone
from datetime import timedelta
from django_celery_beat.models import PeriodicTask, CrontabSchedule

@shared_task(bind = True)
def send_mail_func(self, **kwargs):
    print('passing arguments:', kwargs, type(kwargs))
    # User = get_user_model()
    # users = User.objects.all()
    # # timezone.localtime(users.date_time) + timedelta(days=2)
    # for user in users:
    #     mail_subject = 'Hi! Celery Testing'
    #     message = 'Hi! This is a test email from Celery.'
    #     mail_to = user.email
    #     send_mail(mail_subject, message, settings.EMAIL_HOST_USER, [mail_to], True)
    mail_subject = 'Hi! Celery Testing'
    message = 'Hi! This is a test email from Celery.'
    mail_to = kwargs['email']
    send_mail(mail_subject, message, settings.EMAIL_HOST_USER, [mail_to], True)
    PeriodicTask.objects.filter(name = kwargs['periodic_task_name']).delete()
    return 'Email Sent'