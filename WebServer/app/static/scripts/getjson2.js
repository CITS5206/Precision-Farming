var latlngs = [];

var getJson = async (callback) => {
    var res = await fetch('/getJson', {cache: "no-cache"});
    var resJson = await res.json();
    //console.log(resJson);
    latlngs = resJson;
    console.log(latlngs);
    callback();
    
    // .then(function (text) {
    //     console.log('GET response:');
    //     console.log(text); 
    // });
};

// var getlatlongjson = function () {
//     var polylist = [];
    
//     getJson().then(function (result) {
//         var response = JSON.parse(result);
        
//         Object.keys(response).forEach(function(key) {                   
//             var latlonglist = [];
//             latlonglist[0] = parseFloat(key);
//             latlonglist[1] = parseFloat(response[key]["LONd"]);
//             polylist.push(latlonglist);
//             //console.log(latlonglist);
//             //console.log(polylist);          
            
//             //console.log('lat: ' + key + ', long: ' + response[key]["LONd"]);
//         });
//         //console.log(polylist);        
//     });
//     return polylist
// };

// //getlatlongjson();
//setInterval(getJson, 2000);