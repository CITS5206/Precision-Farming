/**
 * Created by Carson Wood on 6/23/2017.
 */

var map; //Leaflet map
var tilesLoaded = false; //Boolean used to wait for tiles to load before taking screengrab.
var cpos;


$(document).ready(function(){
    initMap();
    cpos = L.circle([ -31.977438961,115.81716941666667], {
        color: "blue",
        fillColor: "#f03",
        fillOpacity: 0.85,
        radius: .75,
        
    }).addTo(map);
  
});

// setInterval(function load() {
//     fetch('d.json')
//     .then(response => response.json())
//     .then(data => document.getElementById("demo").innerHTML= data.latlng);
    
//   },100)

/**
 * Leaflet function to initialize map
 * with tile set, etc.
 */
function initMap() {
    map = L.map('mapid').setView([ -31.977438961,115.81716941666667], 18);
    L.tileLayer('map/{z}/{x}/{y}.png?', {
        attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
        maxZoom: 24,
        id: 'mapbox.satellite',
    }).addTo(map);
    tilesLoaded = true; 
    
}

setInterval(function load() {
    fetch('d.json')
    .then(response => response.json())
    .then(data => {
        trackpos = data.LatLongs
        pos = data.live
        console.log(pos)
        polyline = L.polyline(trackpos).addTo(map);
        cpos.setLatLng(pos)
        

    });
    
  },1000)

