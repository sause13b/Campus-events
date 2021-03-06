var map;
var g_corps = [];
var g_events = [];
var infowindow = [];
var next_events = [];
var tags_to_hide = [];

function my_map() {
    var corps = [
        ['Корпус 1', 43.02778587838957, 131.88849080275082],
        ['Корпус 2', 43.029170, 131.888055],
        ['Корпус 3', 43.030539, 131.888064],
        ['Корпус 4', 43.031968, 131.888519],
        ['Корпус 5', 43.033256, 131.889451],
        ['Корпус 6.1', 43.032676, 131.886519],
        ['Корпус 6.2', 43.033961, 131.887440],
        ['Корпус 7.1', 43.030151871919635, 131.8857342378549],
        ['Корпус 7.2', 43.031411, 131.885960],
        ['Корпус 8.1', 43.02733508254129, 131.88649313302278],
        ['Корпус 8.2', 43.028695, 131.885909],
        ['Корпус 9', 43.025090, 131.899223],
        ['Корпус 10', 43.026180116068346, 131.90138208889158],
        ['Корпус 11', 43.02745779741024, 131.90254512826343],
        ['Корпус 11', 43.02745779741024, 131.90254512826343],
        ['Корпус S', 43.0263366658691, 131.89007994335407],
        ['Корпус G', 43.025547, 131.888958],
        ['Корпус D', 43.02574307342375, 131.89171314627205],
        ['Корпус B', 43.024663, 131.892399],
        ['Корпус A', 43.024608, 131.893769],
        ['Корпус С', 43.02395697096063, 131.89453074526955],
        ['Корпус E', 43.024480, 131.895586],
        ['Корпус F', 43.024417, 131.897502],
    ];

    const campus_bounds = {
        north: 43.041900,
        south: 43.017781,
        west: 131.866455,
        east: 131.921826,
    }

    var options = {
        center: new google.maps.LatLng(43.02914569080389, 131.8904930008918),
        restriction: {
            latLngBounds: campus_bounds,
            strictBounds: false,
        },
        zoom: 16,
        minZoom: 15,
        maxZoom: 19,
        mapId: 'b592755503adfa8a',
    }
    map = new google.maps.Map(document.getElementById("map"), options);
    for(let i = 0; i < events.length; i++) {
        let url = "/eventform/"+events[i]["id"]
        let newLatLng = new google.maps.LatLng(events[i]['lat'], events[i]['lng']);
        let marker = new google.maps.Marker({
            position: newLatLng,
            map: map,
            category: events[i]['tags'],
            title: events[i]['name'],
            icon: {
                url: '/static/map/icons/red.png',
                scaledSize: new google.maps.Size(45, 45),
            },
        });
        g_events.push(marker);
        let content = marker.title + '<br>' + 'Участников: ' + events[i]['count'] +'/'+ events[i]['members'] + '<br>' + '<a href="'+url+'">'+'Подробнее...'+'</a>';
        infowindow[i] = new google.maps.InfoWindow({
            content: content,
        });
        marker.addListener("click", function() {
            infowindow[i].open(map, marker);
        });
    }

    for(let i = 0; i < corps.length; i++) {
        let newLatLng = new google.maps.LatLng(corps[i][1], corps[i][2]);
        let url_;
        if (i <= 14) {
            url_ = '/static/map/icons/orange.png';
        }
        if (i > 14) {
            url_ = '/static/map/icons/green.png'
        }
        let marker = new google.maps.Marker ({
            position: newLatLng,
            map: map,
            label: {
                text :corps[i][0],
                color: 'slategray',
                fontSize: '13',
            },
            icon: {
                url: url_,
                scaledSize: new google.maps.Size(36, 36),
                labelOrigin: new google.maps.Point(-22, 15),
            }
        })
        g_corps.push(marker);
    }
}

window.onload = function() {
    let ul = document.getElementById('events_list')
    for (let i = 0; i < events.length; i++) {
        let name = events[i]['name'];
        let date = events[i]['date'];
        let name_span = document.createElement('span');
        let date_span = document.createElement('span');
        name_span.appendChild(document.createTextNode(name));
        date_span.appendChild(document.createTextNode(date));
        let url = "/eventform/"+events[i]["id"];
        let a = document.createElement('a');
        a.href = url;
        a.appendChild(name_span);
        a.appendChild(date_span);
        a.classList.add('ev');
        a.target = "_blank";
        let li = document.createElement('li');
        li.appendChild(a);
        li.classList.add('event');
        li.classList.add('show_none');
        ul.appendChild(li);
    }


    let ev = document.getElementsByClassName('event');
    for(let i = 0; i < ev.length; i++) {
        ev[i].addEventListener("click", function(){
            let name = this.firstChild.textContent;
            this.classList.add('clicked_event');
            for(let sibling of this.parentNode.children) {
                if (sibling != this) {
                    sibling.classList.remove('clicked_event');
                }
            }
            // for(let i = 0; i < g_events.length; i++) {
            //     infowindow[i].close();
            //     if (g_events[i].title == name) {
            //         g_events[i].setVisible(true);
            //         map.panTo(g_events[i].position);
            //         infowindow[i].open(map, g_events[i]);
            //     }
            // }
        })
    }

    map.addListener("drag", function(){
        for(let i = 0; i < ev.length; i++) {
            ev[i].classList.remove('clicked_event');
        }
        for(let i = 0; i < g_events.length; i++) {
            infowindow[i].close();
        }
    })

    var min_ = Math.min(events.length, 5);
    for(let i = 0; i < min_; i++) {
        ev[i].classList.remove('show_none');
        next_events.push(ev[i]);
    }
    var showed = min_;

    var tags = document.getElementsByClassName("tag");
    for(let i = 0; i < tags.length; i++) {
        tags[i].addEventListener("click", function(){
            this.classList.toggle('clicked_tag');
            let tag = tags[i].textContent;
            var visibility = true;
            if (this.classList.contains('clicked_tag') == true) {
                visibility = false;
                tags_to_hide.push(tag);
                for(let j = 0; j < ev.length; j++) {
                    if (events[j]['tags'].includes(tag) && !ev[j].classList.contains('show_none')) {
                        ev[j].classList.add('show_none');
                        showed--;
                    }
                }
                if (showed < min_) {
                    for(let j = 0; j < ev.length; j++) {
                        var show = 1;
                        for(let k = 0; k < tags_to_hide.length; k++) {
                            let tag_ = tags_to_hide[k];
                            if (events[j]['tags'].includes(tag_)) {
                                show = 0;
                                break;
                            }
                        }
                        if (show == 1 && ev[j].classList.contains('show_none')) {
                            ev[j].classList.remove('show_none');
                            showed++;
                            if (showed == min_) {
                                break;
                            }
                        }
                    }
                }
            }
            else {
                let indx = tags_to_hide.indexOf(tag);
                tags_to_hide.splice(indx,1);

                for(let j = 0; j < ev.length; j++) {
                    var show = 1;
                    for(let k = 0; k < tags_to_hide.length; k++) {
                        let tag_ = tags_to_hide[k];
                        if (events[j]['tags'].includes(tag_)) {
                            show = 0;
                            break;
                        }
                    }
                    if (events[j]['tags'].includes(tag) && show == 1) {
                        ev[j].classList.remove('show_none');
                        showed++;
                        if (showed == min_) {
                            break;
                        }
                    }
                }
            }

            if (showed > min_) {
                for(let j = ev.length-1; j >= 0; j--) {
                    if (!ev[j].classList.contains('show_none')) {
                        ev[j].classList.add('show_none');
                        showed--;
                        if (showed == min_) {
                            break;
                        }
                    }
                }
            }

            for(let j = 0; j < g_events.length; j++) {
                if (visibility == false) {
                    if (g_events[j].category.includes(tag)) {
                        g_events[j].setVisible(visibility);
                        infowindow[j].close(map, g_events[j]);
                    }
                }
                else {
                    var show = 1;
                    for(let k = 0; k < tags_to_hide.length; k++) {
                        let tag_ = tags_to_hide[k];
                        if (g_events[j].category.includes(tag_)) {
                            show = 0;
                            break;
                        }
                    }
                    if (show == 1) {
                        g_events[j].setVisible(visibility);
                    }
                }
            }
        })
    }

    map.addListener("zoom_changed", function(){
        if(map.getZoom() == 15) {
            for (let i = 0; i < g_corps.length; i++) {
                g_corps[i].setVisible(false);
            }
        }
        else if(map.getZoom() > 15) {
            for(let j = 0; j < corps_legend.length-1; j++) {
                let name = corps_legend[j].textContent.slice(3);
                let img = corps_legend[j].querySelector('img');
                if (name == 'Жилые корпуса' && img.classList.contains('gray_filter') == false) {
                    for (let i = 0; i < 14; i++) {
                        g_corps[i].setVisible(true);
                    }
                }
                if (name == 'Учебные корпуса' && img.classList.contains('gray_filter') == false) {
                    for (let i = 14; i < g_corps.length; i++) {
                        g_corps[i].setVisible(true);
                    }
                }
            }
        }
    })

    var corps_legend = document.getElementsByClassName("legend_unit");
    for(let i = 0; i < corps_legend.length; i++) {
        corps_legend[i].addEventListener("click", function(){
            let name = this.textContent.slice(3);
            let img = this.querySelector('img');
            this.classList.toggle('hidden_marker');
            img.classList.toggle('gray_filter');
            if (name == 'Жилые корпуса') {
                for(let i = 0; i < 15; i++) {
                    if (img.classList.contains('gray_filter') == false && map.getZoom() > 15) {
                        g_corps[i].setVisible(true);
                    }
                    else {
                        g_corps[i].setVisible(false);
                    }
                }
            }
            else if (name == 'Учебные корпуса') {
                for(let i = 15; i < g_corps.length; i++) {
                    if (img.classList.contains('gray_filter') == false && map.getZoom() > 15) {
                        g_corps[i].setVisible(true);
                    }
                    else {
                        g_corps[i].setVisible(false);
                    }
                }
            }
            else if (name == 'Эвенты') {
                for(let k = 0; k < tags.length; k++) {
                    if (img.classList.contains('gray_filter') == false) {
                        tags[k].classList.remove('clicked_tag');
                    }
                    else {
                        tags[k].classList.add('clicked_tag');
                    }
                }
                for(let i = 0; i < g_events.length; i++) {
                    if (img.classList.contains('gray_filter') == false) {
                        g_events[i].setVisible(true);
                    }
                    else {
                        g_events[i].setVisible(false);
                    }
                }
            }
        })
    }
}
