from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder
from createEvent.models import *
from django.contrib.auth.decorators import login_required
import datetime
import json



@login_required(login_url='login')
def render_map(request):
    today = datetime.datetime.today()
    today = datetime.date(today.year, today.month, today.day)
    tags = Tag.objects.all()
    events = Event.objects.all().filter(date__gte=today).order_by('date')
    events = events.values()
    # next_events = events.order_by('date').values()
    events = json.dumps(list(events), cls=DjangoJSONEncoder)
    # next_events = json.dumps(list(next_events), cls=DjangoJSONEncoder)
    ev = json.loads(events)
    for i in range(len(ev)):
        ev[i]["tags"] = []

    for tag in tags:
        events_tag = Event.objects.filter(tags__name=tag)
        for event in events_tag:
            id = event.id
            i = 0
            for dict in ev:
                if dict["id"] == id:
                    ev[i]['tags'].append(tag.name)
                i += 1

    events = json.dumps(ev)
    data = {'tags': tags, 'events': events}
    return render(request, 'map/index.html', data)
