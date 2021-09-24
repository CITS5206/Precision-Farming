//import get_latlong from "./get_latlong.js"
const get_latlong = require("./get_latlong.js");
const returnData = require("./get_latlong.js");
const callback = require("./get_latlong.js");

// test('GET json from server', async () => {
//     const response = await get_latlong(returnData);
//     console.log(await response);
//     expect(await response.length).toBe(5);
//     done()
// });

test('GET json from server', done => {
    function returnData(data) {
      try {
        expect(data.length).toBe(5);
        done();
      } catch (error) {
        done(error);
      }
    }
  
    get_latlong(returnData);
  });