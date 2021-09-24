
import "core-js/stable";
import "regenerator-runtime/runtime";
var XMLHttpRequest = require('xhr2');
// const axios = require('./axiosConfig');
global.TextEncoder = require("util").TextEncoder;
global.TextDecoder = require("util").TextDecoder;

// //const jsdom = require('jsdom');
var { JSDOM } = require('jsdom');
var { window }= new JSDOM();
// global.$ = global.jQuery = $;
var $ = require('./jquery-3.6.0')(window);





/** Using jQuery ajax */
// function get_latlong() {
//     var var1 = [{ "test" : 1}]
//     $.ajax({
//         url: "http://localhost:8080/latlong_data/latlong.json",
//         method: "GET",
//         async: true,
//         cache: false,

//         success: function (response) {
            
//             var1 = response;
//             text_var1 = JSON.stringify(var1);
//             $(".display_latlong").html(text_var1);
//             console.log(var1);
//         },
//         error: function(xhr, status, error){
//             var errorMessage = xhr.status + ': ' + xhr.statusText;
//             $(".display_latlong").html('Error - ' + errorMessage)
//         }
    
//     });
//     console.log("done");
//     return var1;
// };

function returnData(responsedata) {
    // var respJSON = JSON.parse(responsedata)
    console.log(responsedata);
    return responsedata
};

/** Using pure javascript */

var url = "http://localhost:8080/latlong_data/latlong.json?nocache=" + new Date().getTime();
function get_latlong(callback) {
    var xhr = new XMLHttpRequest();
    xhr.responseType = 'json'
    xhr.open('GET', url, true);
    xhr.onreadystatechange = function() {
        if(xhr.readyState === XMLHttpRequest.DONE) {
            var status = xhr.status;
            if (status === 0 || (status >= 200 && status < 400)) {
                // console.log('return');
                // var var1 = xhr.responseText;
                // response = xhr.responseText;
                // text_var1 = JSON.stringify(var1);
                //$(".display_latlong").html(var1);
                // console.log(xhr.response);
                callback(xhr.response);}
            else {
                var errorMessage = xhr.status + ': ' + xhr.statusText;
                $(".display_latlong").html('Error - ' + errorMessage)
                }

            
        };
    };
    xhr.send();
    // console.log('done');
    
};

module.exports = get_latlong;

// var ajax_call = function () {
//     $.ajax({
//         url: "ajax.json",
//         method: "GET",
//         async: true,

//         }).then(function (response) {
//             console.log(response);
//             if (! response == var1) {
//                 var1 = response
//                 console.log(var1);
//             }
//         });
    
//     };


// var display_latlong = function () {
//     $(".display_latlong").html(text_var1);
// };

//setInterval(get_latlong, 2000);

get_latlong(returnData);

