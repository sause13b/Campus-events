from django.shortcuts import render
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from createEvent.models import *
from django.contrib.auth.decorators import login_required
import json

@login_required(login_url='login')
def render_map(request):
    tags = Tag.objects.all()
    events = Event.objects.all().values()
    next_events = events[:10]
    events = json.dumps(list(events), cls=DjangoJSONEncoder)
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
    print(events)
    data = {'tags': tags, 'next_events': next_events, 'events': events}
    return render(request, 'map/index.html', data)
