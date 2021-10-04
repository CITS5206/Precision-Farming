//create a map the center coordinates will need to be changed to get them from user
var map = L.map( 'map', {
    center: [-31.9774381775,
        115.817171354],
    minZoom: 0,
    zoom: 30
    });
 
//initiate a layer    
function initMap() {   
       
    L.tileLayer('/static/maps/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
        subdomains: ['a','b','c'],
        maxNativeZoom: 19,
        maxZoom: 25
        }).addTo( map );
};

//polyline
var polyline = L.polyline(latlngs, {color: 'red'}).addTo(map);


function addLine() {
        getJson(function () {
            //check that coordinates is correct in console
            console.log(latlngs);
            //remove previous polyline
            polyline.removeFrom(map);
            //add new polyline
            polyline = L.polyline(latlngs, {color: 'red'}).addTo( map );
            })
    
};

$(document).ready(function() {initMap();});

//call every 2s
setInterval(addLine, 2000);
