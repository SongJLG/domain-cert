# from django.shortcuts import render

# Create your views here.

# from apscheduler.schedulers.background import BackgroundScheduler
# from cert.api import tasks
# scheduler = BackgroundScheduler(timezone='Asia/Shanghai')
# scheduler.add_job(func=tasks.refresh_certs_messages_to_db, trigger="cron", minute='*', id="test_cron")
# scheduler.start()

from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from .api import tasks
scheduler = BackgroundScheduler(timezone='Asia/Shanghai')
scheduler.add_jobstore(DjangoJobStore(), 'default')
scheduler.add_job(func=tasks.refresh_certs_messages_to_db, trigger="cron", day='*', id="cret_update_daily")
register_events(scheduler)
scheduler.start()