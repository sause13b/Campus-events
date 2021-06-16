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
    var g_corps = []

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
                    fontSize: '10',
                },
                icon: {
                    url: url_,
                    scaledSize: new google.maps.Size(25, 25),
                    labelOrigin: new google.maps.Point(-22, 15),
                }
        })
        g_corps.push(marker);
    }

    let newLatLng = new google.maps.LatLng(lat, lng);
    let marker = new google.maps.Marker ({
        position: newLatLng,
        map: map,
    })
    map.panTo(newLatLng)
}