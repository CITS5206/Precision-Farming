from app        import app, db
from flask      import render_template
from app.models import Map

@app.route('/tracking')
def tracking():
    # TODO: func: python - device-status
    sensor = 'up'
    gps = 'down'
    # TODO: func: get A, B coordinate
    pointA = '-40.678901, 163.8765432'
    pointB = '-40.678901, 163.8765432'
    # TODO: func: python - get current-location
    currentLat = '-31.980945378411835'
    currentLong = '115.81819424545051'
    return render_template('tracking.html', 
                            sensor=sensor, gps=gps,
                            pointA=pointA, pointB=pointB,
                            currentLat=currentLat, currentLong=currentLong)

@app.route('/')
@app.route('/index')
def index():
    mapLst = Map.query.all()
    return render_template('index.html')

@app.route('/history')
def history():
    # lstHistory = History.query.all()
    return render_template('history.html')

@app.route('/map')
def map():
    lstMap = Map.query.all()
    return render_template('map.html', lstMap=lstMap)