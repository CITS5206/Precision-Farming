from app        import app
from flask      import render_template, redirect, url_for, request
from app.models import Map
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
