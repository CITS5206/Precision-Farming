function returnData(resp) {
    console.log(resp)
};

function getData(callback) {
    var a;
    setTimeout(function () {
        a=5;
        callback(a);
    },10);
    console.log(a);
    return a;    
};

var b = getData(returnData);
console.log(b);