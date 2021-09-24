const axios = require('axios');

const axiosInstance = axios.default.create({
    baseURL: 'http://fakeserver.precisionfarming.com/latlong_data'
});

module.exports = axiosInstance;