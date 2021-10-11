var map = L.map('map').setView(currPos, 18.0);

var baseLayer = L.tileLayer('http://localhost:5000/static/maps/'+ mapName +'/{z}/{x}/{y}.png', {
                    minZoom: 8,
                    maxZoom: 20,
                    tms: false,
                    attribution: 'Generated by TilesXYZ'
                }).addTo(map);
var markerLayer = L.circle(currPos, {
                    color: "blue",
                    fillColor: "#f03",
                    fillOpacity: 0.85,
                    radius: 1.25
                }).addTo(map);

var latlngs = []
var polyline = L.polyline(latlngs, {color: 'red'}).addTo(map);
var eleCurrPos = document.getElementById('current-position');
var resJson

var cfg = {
    // // radius should be small ONLY if scaleRadius is true (or small radius is intended)
    "radius": 15,
    "maxOpacity": .8, 
    // // scales the radius based on map zoom
    "scaleRadius": false, 
    // // if set to false the heatmap uses the global maximum for colorization
    // // if activated: uses the data maximum within the current map boundaries 
    // //   (there will always be a red spot with useLocalExtremas true)
    "useLocalExtrema": true,
    // // which field name in your data represents the latitude - default "lat"
    // latField: 'lat',
    // // which field name in your data represents the longitude - default "lng"
    lngField: 'lng',
    // // which field name in your data represents the data value - default "value"
    valueField: measure
};

var heatmapLayer = new HeatmapOverlay(cfg).addTo(map);

var getJson = async (callback) => {
    var res = await fetch('/getJson', {cache: "no-cache"});
    resJson = await res.json();
    // latlngs = resJson['LatLongs']
    currPos = resJson['live'];
    callback();
};

function draw() {
    getJson(function () {
        // polyline = L.polyline(latlngs, {color: 'red'}).addTo( map );
        markerLayer.setLatLng(currPos);
        heatmapLayer.setData(resJson);
        })
};

setInterval(draw, 250);
// function tracking() {
//     var btn_track =  document.getElementById('btn-track');
//     if (btn_track.innerHTML == 'View live'){
//         btn_track.innerHTML = 'Stop';
//         draw_Interval = setInterval(draw, 1000);
//     } else {
//         // btn_track.href =Flask.url_for('finishTrack', {'mapid': mapid});
//         btn_track.innerHTML = 'Done';
//         clearInterval(draw_Interval);
//     }
// }
