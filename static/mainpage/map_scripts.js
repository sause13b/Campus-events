function my_map() {
    var events = [
        ['0', 'D&D', 43.03267057306809, 131.89137918437376, 'настолки'],
        ['1', 'Играю на гитаре', 43.028535518689694, 131.8978870599067, 'гитара'],
    ];
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
    var g_corps = [];
    var g_events = [];
    var infowindow = [];

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
    var map = new google.maps.Map(document.getElementById("map"), options);

    for(let i = 0; i < events.length; i++) {
        let newLatLng = new google.maps.LatLng(events[i][2], events[i][3]);
        let marker = new google.maps.Marker({
            position: newLatLng,
            map: map,
            category: events[i][4],
            title: events[i][1],
            icon: {
                url: 'icons/red.png',
                scaledSize: new google.maps.Size(45, 45),
            },
        });
        g_events.push(marker);

        infowindow[i] = new google.maps.InfoWindow({
            content: marker.title,
        });
        marker.addListener("click", function() {
            infowindow[i].open(map, marker);
        });
    }

    for(let i = 0; i < corps.length; i++) {
        let newLatLng = new google.maps.LatLng(corps[i][1], corps[i][2]);
        let url_;
        if (i <= 14) {
            url_ = 'icons/orange.png';
        }
        if (i > 14) {
            url_ = 'icons/green.png'
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


    var tags = document.getElementsByClassName("tag");
    for(let i = 0; i < tags.length; i++) {
        tags[i].addEventListener("click", function(){
            this.classList.toggle('clicked_tag');
            let tag = tags[i].textContent.slice(1);
            var visibility = true
            if (this.classList.contains('clicked_tag') == true) {
                visibility = false
            }
            for(let i = 0; i < g_events.length; i++) {
                if (g_events[i].category == tag) {
                    g_events[i].setVisible(visibility);
                    if (g_events[i].visible != true) {
                        infowindow[i].close(map, g_events[i]);
                    }
                }
            }
        })
    }

    var next_events = document.getElementsByClassName("event");
    for(let i = 0; i < next_events.length; i++) {
        next_events[i].addEventListener("click", function(){
            let name = this.textContent.slice(0, -10);
            this.classList.add('clicked_event');
            for(let sibling of this.parentNode.children) {
                if (sibling != this) {
                    sibling.classList.remove('clicked_event');
                }
            }
            for(let i = 0; i < g_events.length; i++) {
                infowindow[i].close();
                if (g_events[i].title == name) {
                    g_events[i].setVisible(true);
                    //map.setZoom(17);
                    map.panTo(g_events[i].position);
                    infowindow[i].open(map, g_events[i]);
                }
            }
        })
    }

    map.addListener("drag", function(){
        for(let i = 0; i < next_events.length; i++) {
            next_events[i].classList.remove('clicked_event');
        }
        for(let i = 0; i < g_events.length; i++) {
            infowindow[i].close();
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
                    tags[k].classList.toggle('clicked_tag');
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

    map.addListener("zoom_changed", function(){
        if(map.getZoom() == 15) {
            for (let i = 0; i < corps.length; i++) {
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
}
//TODO:
