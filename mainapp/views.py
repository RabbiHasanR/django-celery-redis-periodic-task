from django.http import HttpResponse
from django.shortcuts import render
from .tasks import test_func
from send_mail.tasks import send_mail_func
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json

# Create your views here.

def test(request):
    test_func.delay()
    return HttpResponse('Task Completed')

def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse('Email Sent')

def schedule_mail(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour = 12, minute = 32)
    print(schedule, created)
    periodc_task_name = 'Send_Mail_to_All'+'_11'
    task = PeriodicTask.objects.create(name = periodc_task_name, task = 'send_mail.tasks.send_mail_func', crontab = schedule,
    kwargs=json.dumps({'email': 'jasrabbi50@gmail.com', 'periodic_task_name': periodc_task_name, 'schedule': 'test'}))
    return HttpResponse('Done')
