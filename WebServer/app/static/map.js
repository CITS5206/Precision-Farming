var map = L.map('map').setView([currentLat, currentLong], 16.0);

L.tileLayer('http://localhost:5000/static/'+ mapName +'/{z}/{x}/{y}.png', {
        minZoom: 8,
        maxZoom: 20,
        tms: false,
        attribution: 'Generated by TilesXYZ'
    }).addTo(map);
L.marker([currentLat, currentLong]).addTo(map)
    .openPopup();


var latlngs = [];
var polyline = L.polyline(latlngs, {color: 'red'}).addTo(map);

var getJson = async (callback) => {
    var res = await fetch('/getJson', {cache: "no-cache"});
    var resJson = await res.json();
    latlngs = resJson;
    //check correct coordinates in browser's console
    console.log(latlngs);
    //draw polyline when done
    callback();
};


function addLine() {
    getJson(function () {
        polyline.removeFrom(map);
        polyline = L.polyline(latlngs, {color: 'red'}).addTo( map );
        })
};



function tracking() {
    let btn_track =  document.getElementById('btn-track')
    if (btn_track.innerHTML == 'Start Tracking'){
        btn_track.innerHTML = 'Stop and Save'
        // TODO: func: js read json, draw lines and current location
        addLine_Interval = setInterval(addLine, 2000);
    } else {
        btn_track.innerHTML = 'Start Tracking'
        // TODO: Stop function drawing
        clearInterval(addLine_Interval);
    }
    
}

function stopTracking() {
    clearInterval(addLine_Interave);
}
