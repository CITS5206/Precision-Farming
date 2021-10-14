'''
 The University of Western Australia : 2021

* CITS5206 Professional Computing

* Group: Precision Farming



* Source Code

* Author: Harper Wu

* Co-Author: Kiet Hoang

* Date Created: 23-09-2021

* Last Modified: 13-10-2021

* Version: 1.0

* State : Stable 
'''

from app        import app
from flask      import render_template, request
import json
import os
import socket

@app.route('/tracking/')
def tracking():
    mapName = request.args.get('mapName')
    measure = request.args.get('measure')
    currPos = getJson()['live']
    ip=getIP()
    return render_template('tracking.html', title='PrecisionFarming-Tracking', 
                            measure = measure, currPos = currPos, mapName=mapName,
                            ip=ip)


@app.route('/index')
def index():
    return render_template('index.html', title='PrecisionFarming-Home')


@app.route('/heatmap')
def heatmap():
    return render_template('heatmap.html', title='Heatmap')

@app.route('/')
@app.route('/map')
def map():
    lstMap = getMapNames()
    return render_template('map.html', title='PrecisionFarming-Map', lstMap=lstMap)

@app.route('/getJson')
def getJson(path='./leaflet-demo/d.json'):
    f = open(path, 'r')
    data = json.load(f)
    return data

def getMapNames():
    # TODO: Try Catch path not exist
    # TODO: Test@Clariza
    maps = []
    entries = os.listdir('./app/static/maps')
    for e in entries:
        if not e.startswith('.'):
            maps.append(e)
    return maps

def getIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
