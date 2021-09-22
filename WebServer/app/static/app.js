
function tracking() {
    let btn_track =  document.getElementById('btn-track')
    if (btn_track.innerHTML == 'Start Tracking'){
        btn_track.innerHTML = 'Stop Tracking'
    } else {
        btn_track.innerHTML = 'Start Tracking'
    }

}