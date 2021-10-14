/*
The University of Western Australia : 2021
CITS5206 Professional Computing
Group: Precision Farming

Source Code
Author: Tuan Kiet Hoang
Co-Author: 
Date Created: 30/09/2021    
Last Modified: 04/10/2021
Version: [Major Versions needs to be pushed in Github!]
State : [Beta, Stable]
*/

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