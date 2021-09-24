## Web server for precision farming app
This web server uses Flask development framework

## App description
The app provides the ability to track the GPS location in real-time on a map without internet connection. It also provides the combined read data from a Dualem sensor and a GPS in scv format.

## Current functionality
- Read input data from sensors
- Combine input data to csv
- Allow user to choose location of files and map tiles
- Display tracking on a web page with zooming map

## Getting started
Currently the app is still in development, it can be be deployed in a development environment.

The requirements are in requirements.txt

To install the required packages: $pip install -r requirements.txt

To run the app: $flask run 

This should start the app running on localhost at port 5000, i.e. [http://localhost:5000/] and [http://localhost:5000/index]

To run the app on a specific local IP to gain access through other local devices such as smartphones, tablets: $flask run -h [your_local_IP_of_the_deployment_device]
This should start the app running on (http://[your_IP]:5000/) and (http://[your_IP]:5000/index)

To stop the app: $^C

## Prerequisites
Requires python 3.8, flask, pyserial, pynmea

## Deloyment
via localhost

## Authors
.
.
.
.
.
