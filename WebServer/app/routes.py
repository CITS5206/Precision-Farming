'''
 The University of Western Australia : 2021

* CITS5206 Professional Computing

* Group: Precision Farming



* Source Code

* Author: Harper Wu

* Co-Author: Tuan Kiet Hoang

* Date Created: 23-09-2021

* Last Modified: 13-10-2021

* Version: 1.0

* State : Stable 
'''

from app        import app
from flask      import render_template, request
import json
import os
from pathlib    import Path

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
    # TODO: Test@Clariza
    dir = './app/static/maps'
    Path(dir).mkdir(parents=True, exist_ok=True)
    maps = []
    try:
        entries = os.listdir(dir)
        for e in entries:
            if not e.startswith('.'):
                maps.append(e)
    except:
        pass
    return maps
