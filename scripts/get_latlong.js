var get_latlong = function () {
    $.ajax({
        url: "latlong_data/latlong.json",
        method: "GET",
        async: true,
        cache: false,

        }).then(function (response) {
            
            var1 = response
            text_var1 = JSON.stringify(var1);
            console.log(var1);
        });
    
    };

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


var display_latlong = function () {
    $(".display_latlong").html(text_var1);
};

setInterval( function () {
    get_latlong();
    display_latlong();
 }, 2000);

