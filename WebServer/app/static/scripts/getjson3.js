var latlngs = [];
var pos;

var getJson = (callback) => {
    fetch('/getJson', {cache: "no-cache"})
    .then((response) => response.json())
    .then((resObj) => {
        latlngs = resObj.pos;
        pos = resObj.currentPos;
    });
        
    //check correct coordinates in browser's console
    //console.log(pos);
    //console.log(latlngs);
    
    //draw polyline when done
    callback();
};