/* 
* The University of Western Australia : 2021

* CITS5206 Professional Computing

* Group: Precision Farming



* Source Code

* Author: Harper Wu

* Co-Author: Tuan Kiet Hoang

* Date Created: 30-09-2021

* Last Modified: 13-10-2021

* Version: 1.0

* State : Stable
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

var getJson = async (callback) => {
    var res = await fetch('/getJson', {cache: "no-cache"});
    resJson = await res.json();
    currPos = resJson['live']
    latlngs = resJson['LatLongs']
    console.log(latlngs)
    callback();
};

function draw() {
    getJson(function () {
        markerLayer.setLatLng(currPos);
        polyline = L.polyline(latlngs, {color: 'red'}).addTo(map);
    })
};

draw_Interval = setInterval(draw, 250);

$('#saveImage').click(async function () {
    var saveImage = document.getElementById('saveImage');
    if (saveImage.innerHTML ==='Stop'){
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