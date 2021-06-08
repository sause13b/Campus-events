from django.shortcuts import render


def render_map(request):
    test_tags = ['#настолки', '#гитара']
    test_next_events = [
        {'name': 'D&D', 'date': '06.06.2021'},
        {'name': 'Играю на гитаре', 'date': '06.06.2021'}
    ]
    test_events = [
        ['0', 'D&D', 43.03267057306809, 131.89137918437376, 'настолки'],
        ['1', 'Играю на гитаре', 43.028535518689694, 131.8978870599067, 'гитара'],
    ];

    data = {'tags': test_tags, 'next_events': test_next_events, 'events': test_events}

    return render(request, 'map/index.html', data)
