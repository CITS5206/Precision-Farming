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
Open python GUI, connect hardwares and click "START WEBSERVER", then access web application via browser . (Ongoing development)