function addLine() {
    // getJson(function () {
    //     console.log(latlngs);
    //     polyline.removeFrom(map);
    //     polyline = L.polyline(latlngs, {color: 'red'}).addTo( map );
    //     })

var latlngs = [[-31.979535, 115.817553],[-31.979535, 115.817653]];
console.log(latlngs);
L.polyline(latlngs, {color: 'red'}).addTo( map );


};

function tracking() {
    let btn_track =  document.getElementById('btn-track')
    if (btn_track.innerHTML == 'Start Tracking'){
        btn_track.innerHTML = 'Stop and Save'
        // TODO: func: js read json, draw lines and current location
        setInterval(addLine, 2000);
    } else {
        btn_track.innerHTML = 'Start Tracking'
        // TODO: Stop function drawing
    }
    
}
