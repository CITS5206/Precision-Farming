from app        import app
from flask      import render_template, redirect, url_for, request
from app.models import Map
import json
import os

@app.route('/tracking/')
def tracking():
    mapName = request.args.get('mapName')
    measure = request.args.get('measure')
    currPos = getJson()['live']
    return render_template('tracking.html', title='PrecisionFarming-Tracking', 
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
    entries = os.listdir('./app/static/maps')
    for e in entries:
        if not e.startswith('.'):
            maps.append(e)
    return maps