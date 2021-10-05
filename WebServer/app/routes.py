from app        import app, db
from flask      import render_template
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
    # uwa
    currentLat = '-31.980945378411835'
    currentLong = '115.81819424545051'
    map = Map.query.filter_by(id = mapid).first_or_404()
    return render_template('tracking.html', title='PrecisionFarming-Tracking', 
                            sensor=sensor, gps=gps,
                            pointA=pointA, pointB=pointB,
                            currentLat = currentLat, currentLong =currentLong,
                            map=map)

@app.route('/')
@app.route('/index')
def index():
    # mapLst = Map.query.all()
    return render_template('index.html', title='PrecisionFarming-Home')

@app.route('/history')
def history():
    # lstHistory = History.query.all()
    return render_template('history.html', title='History')

@app.route('/map')
def map():
    lstMap = Map.query.all()
    return render_template('map.html', title='PrecisionFarming-Map', lstMap=lstMap)

@app.route('/getJson')
# def getJson(path='./out2.json'):
def getJson(path='./Generate-JSON/gps-data.json'):
    f = open(path, 'r')
    data = json.load(f)
    return data

@app.route('/finishTrack/<mapid>')
def finishTrack(mapid):
    # TODO: Save csv file
    # TODO: update map name and csv file name into history table
    return render_template('history.html', title='History')