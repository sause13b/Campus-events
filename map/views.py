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
    ev = json.dumps(list(events.values()), cls=DjangoJSONEncoder)
    ev = json.loads(ev)
    for i in range(len(ev)):
        ev[i]["tags"] = []
        ev[i]["count"] = events[i].members_list.count()

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


def render_us(request):
    return render(request, 'anekdot/aboutus.html')