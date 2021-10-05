from app        import app, db
from flask      import render_template, redirect, url_for
from app.models import Map
import json

@app.route('/tracking/<mapid>')
def tracking(mapid):
    # TODO: func: python - device-status
    sensor = 'up'
    gps = 'down'
    # TODO: func: get A, B coordinate
    pointA = '-30.678901, 114.8765432'
    pointB = '-32.678901, 116.8765432'
    # TODO: func: python - get current-location
    currPos = getJson()['CURRENT_POS']
    map = Map.query.filter_by(id = mapid).first_or_404()
    return render_template('tracking.html', title='PrecisionFarming-Tracking', 
                            sensor=sensor, gps=gps,
                            pointA=pointA, pointB=pointB,
                            currPos = currPos,
                            map=map)


@app.route('/index')
def index():
    return render_template('index.html', title='PrecisionFarming-Home')

@app.route('/')
@app.route('/map')
def map():
    lstMap = Map.query.all()
    return render_template('map.html', title='PrecisionFarming-Map', lstMap=lstMap)

@app.route('/getJson')
def getJson(path='./Generate-JSON/gps-data.json'):
    f = open(path, 'r')
    data = json.load(f)
    return data
