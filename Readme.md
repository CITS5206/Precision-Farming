# EMI Toolkit (v1.0)
## Date : 20/09/2021

# Team: 
    1. Arjun Panicker
    2. Clariza Look
    3. Deepakraj Sugumaran
    4. Harper Wu
    5. Kiet Hoang

## Project Sub-Team:
    A. Python Companion App - [ Arjun Panicker , Deepakraj]
    B. Python Websever  - [Clariza Look, Harper Wu, Kiet Hoang]

# Python Companion App

### Python Companion App - Requirements
    1. [Required] Python 3.7.3 and above
    2. [Required] PySerial 3.5 and above
    3. [Required] PyNMEA-2 1.18 and above
### Python Companion App - Install Dependent Packages
    
    pip install requirements.txt
    
    
### Python Companion App - Running the GUI
    1. Download or clone the repo.
    2. Open the Python GUI folder.
    3. run install command from above
    4a. Using terminal : python3 main.py
    4b. Using IDE: Open main.py and RUN.
    


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

