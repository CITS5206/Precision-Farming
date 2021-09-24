var latlngs = [];

var getJson = async (callback) => {
    var res = await fetch('/getJson', {cache: "no-cache"});
    var resJson = await res.json();
    latlngs = resJson;
    //check correct coordinates in browser's console
    console.log(latlngs);
    //draw polyline when done
    callback();
};