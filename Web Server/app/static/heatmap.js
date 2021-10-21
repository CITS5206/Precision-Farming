/* 
* The University of Western Australia : 2021

* CITS5206 Professional Computing

* Group: Precision Farming



* Source Code

* Author: Harper Wu

* Co-Author: Tuan Kiet Hoang

* Date Created: 21-10-2021

* Last Modified: 21-10-2021

* Version: 1.0

* State : Debug
*/


var map = L.map('map').setView(currPos, 18.0);
// To load the local map, need to access server machine ip instead of localhost in broswer
var baseLayer = L.tileLayer('/static/maps/'+ mapName +'/{z}/{x}/{y}.png', {
                    minZoom: 17,
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

var eleCurrPos = document.getElementById('current-position');
var resJson

var cfg = {
    // radius should be small ONLY if scaleRadius is true (or small radius is intended)
    "radius": 15,
    "maxOpacity": .8, 
    // scales the radius based on map zoom
    "scaleRadius": false, 
    // if set to false the heatmap uses the global maximum for colorization
    // if activated: uses the data maximum within the current map boundaries 
    //   (there will always be a red spot with useLocalExtremas true)
    "useLocalExtrema": true,
    // which field name in your data represents the latitude - default "lat"
    latField: 'lat',
    // which field name in your data represents the longitude - default "lng"
    lngField: 'lng',
    // // which field name in your data represents the data value - default "value"
    valueField: measure
    // TODO: explain meaning / color of heatmap
};

var heatmapLayer = new HeatmapOverlay(cfg).addTo(map);

var getJson = async (callback) => {
    var res = await fetch('/getHMJson', {cache: "no-cache"});
    resJson = await res.json();
    currPos = resJson['live']
    callback();
};

function draw() {
    getJson(function () {
        markerLayer.setLatLng(currPos);
        heatmapLayer.setData(resJson);
    })
};

// draw_Interval = setInterval(draw, 250);
draw();

function getYMD(){
    var d = new Date(),
    month = '' + (d.getMonth() + 1),
    day = '' + d.getDate(),
    year = d.getFullYear();

    if (month.length < 2) 
        month = '0' + month;
    if (day.length < 2) 
        day = '0' + day;

    return [year, month, day].join('');
}


$('#saveImage').click(async function () {
    var saveImage = document.getElementById('saveImage');
    if (saveImage.innerHTML ==='Save Image'){
        // map.setZoom(18);
        // await new Promise(r => setTimeout(r, 2000));        
        blob = domtoimage.toBlob(document.getElementById('map'))
            .then(function (blob) {
                let ymd = getYMD();
                // download path depend on the browser setting, javascript can not specify
                // File can not be saved when page has GET error,
                // like 'http://localhost:5000/blah.png 404 (NOT FOUND)'
                window.saveAs(blob, mapName+'_'+measure+'_'+ymd+'.png');
            });
        // clearInterval(draw_Interval);
        saveImage.innerHTML = 'Done';
    }
})
