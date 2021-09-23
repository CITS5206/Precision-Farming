var map = L.map( 'map', {
    center: [-32.5041679, 116.9701738],
    minZoom: 0,
    zoom: 20
    });
    
function initMap() {   
       
    L.tileLayer('/static/maps/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
        subdomains: ['a','b','c']
        }).addTo( map );

    // var latlngs = [
    //     [115.8179331,-31.9800244],
    //     [115.8179330,-31.9800241],
    //     [115.8179332,-31.9800242]
    // ];

    // var polyline = L.polyline(latlngs, {color: 'red'}).addTo(map);
};
var polyline = L.polyline(latlngs, {color: 'red'}).addTo(map);

function addLine() {
        getJson(function () {
            console.log(latlngs);
            polyline.removeFrom(map);
            polyline = L.polyline(latlngs, {color: 'red'}).addTo( map );
            })
    
    //var latlngs = [[-32.5041679, 116.9701738],[-32.5041083, 116.9701581]];
    //console.log(latlngs);
    //L.polyline(latlngs, {color: 'red'}).addTo( map );


};

$(document).ready(function() {initMap();});

//addLine();
setInterval(addLine, 2000);
//setInterval(getlatlngs, 2000);