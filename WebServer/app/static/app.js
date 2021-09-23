
function tracking() {
    let btn_track =  document.getElementById('btn-track')
    if (btn_track.innerHTML == 'Start Tracking'){
        btn_track.innerHTML = 'Stop Tracking'
        // TODO: func: js read json, draw lines and current location
    } else {
        btn_track.innerHTML = 'Start Tracking'
        // TODO: Stop function drawing
    }
    
}