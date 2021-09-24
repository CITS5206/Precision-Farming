# Web Server - Precision Farming
This web server is using Flask to host a web application as a dashboard for users to collect and visualize data from Dualem 1H sensor and external GPS moduel.

## Quick start for developer
1. Install and activate virtual environment
```
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies with pip or pip3
```
pip install -r requirements.txt
```

3. Run flask program in WebServer directory
```
export FLASK_APP=farm.py
flask run
```

## Quick start for client
Option 1. Open python GUI, connect hardwares and click "START WEBSERVER", then access web application via browser.  
Option 2. Use an executable file to open the web application. (Ongoing development)


## Web Application

### Home Page
From home page of this applicaiton, users could use map or history button to view avaiable maps and history data collection record.  

### Map page
In map page, there are a list of maps of different map which could be use to perform data collection and visualization.  
Choose the fild map would like to use to process to viem map and start tracking

### Tracking page
In tracking page, the map selected in previous page would be shown with location coordinate and hardware status informaiton on top and operation button on th bottom.

