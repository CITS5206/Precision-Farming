var get_latlong = function () {
    $.ajax({
        url: "latlong.json",
        method: "GET",
        async: true,
        cache: false,

        }).then(function (response) {
            
            var1 = response
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

setInterval(get_latlong, 2000)

