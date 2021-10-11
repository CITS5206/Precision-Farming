from app        import app
from flask      import render_template, redirect, url_for, request
from app.models import Map
import json
import os

@app.route('/tracking/')
def tracking():
    # TODO: func: python - device-status
    # sensor = 'up'
    # gps = 'down'
    # # TODO: func: get A, B coordinate
    # pointA = '-30.678901, 114.8765432'
    # pointB = '-32.678901, 116.8765432'
    # TODO: func: python - get current-location
    # currPos = [-31.977397621666668,115.81710717183333]
    mapName = request.args.get('mapName')
    measure = request.args.get('measure')
    currPos = getJson()['live']
    # map = Map.query.filter_by(id = mapid).first_or_404()
    return render_template('tracking.html', title='PrecisionFarming-Tracking', 
                            # sensor=sensor, gps=gps,
                            # pointA=pointA, pointB=pointB,
                            measure = measure, currPos = currPos, mapName=mapName)


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
    # print(os.getcwd())
    entries = os.listdir('./app/static/maps')
    for e in entries:
        if not e.startswith('.'):
            maps.append(e)
    return maps