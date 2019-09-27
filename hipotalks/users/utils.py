import datetime

from django.conf import settings

from hipotalks.users.models import User
from hipotalks.events.models import Event

LAST_EVENT_DATE_KEY = 'last_event_date_key'


def next_weekday(date, weekday):
    days_ahead = weekday - date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return date + datetime.timedelta(days_ahead)


def scheduler():
    users = User.objects.filter(is_active=True).order_by('id')
    index = 0
    today = datetime.datetime.today()
    weekday = 3 # Thursday
    date = next_weekday(today.date(), weekday)
    while index <= len(users):
        grouped_users = users[index: index + 3]
        print(grouped_users)
        event = Event.objects.create(
            event_type=Event.EVENT_TYPE_HIPOTALKS,
            date=date,
        )
        event.users.add(*grouped_users)
        settings.REDIS_CONNECTION.setex(LAST_EVENT_DATE_KEY, 60 * 60 * 5, date.strftime("%m-%d-%Y"))
        date += datetime.timedelta(days=7)
        index += 3


def create_scheduler():
    last_event = Event.objects.filter(is_completed=False, is_canceled=False).order_by('-date').first()
    today = datetime.datetime.today().date().strftime("%m-%d-%Y")
    if not last_event or last_event.date.strftime("%m-%d-%Y") == today:
        scheduler()
    settings.REDIS_CONNECTION.setex(LAST_EVENT_DATE_KEY, 60 * 60 * 5, last_event.date.strftime("%m-%d-%Y"))


def update_scheduler(event_id):
    # TODO: Configure scheduler for canceled events and townhall events.
    updated_event = Event.objects.get(id=event_id)
    events = Event.objects.filter(date__gte=updated_event.date).order_by('date')
    for event in events:
        event.date += datetime.timedelta(days=7)
        event.save()
        settings.REDIS_CONNECTION.setex(LAST_EVENT_DATE_KEY, 60 * 60 * 5, event.date.strftime("%m-%d-%Y"))