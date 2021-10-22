'''
 The University of Western Australia : 2021

* CITS5206 Professional Computing

* Group: Precision Farming



* Source Code

* Author: Harper Wu

* Co-Author: Tuan Kiet Hoang

* Date Created: 23-09-2021

* Last Modified: 15-10-2021

* Version: 1.1

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
    # measure = request.args.get('measure')
    currPos = getJson()['live']
    return render_template('tracking.html', title='PrecisionFarming-Tracking', 
                            # measure = measure, 
                            currPos = currPos, mapName=mapName)

@app.route('/heatmap/')
def heatmap():
    mapName = request.args.get('mapName')
    measure = request.args.get('measure')
    currPos = getJson()['live']
    return render_template('heatmap.html', title='PrecisionFarming-Heatmap', 
                            measure = measure, 
                            currPos = currPos, mapName=mapName)

@app.route('/index')
def index():
    return render_template('index.html', title='PrecisionFarming-Home')

@app.route('/')
@app.route('/map')
def map():
    lstMap = getMapNames()
    return render_template('map.html', title='PrecisionFarming-Map', lstMap=lstMap)

@app.route('/getJson')
def getJson(path='./app/static/liveFeed/data.json'):
    '''
    getJson
        :parameters:
            string, path of th file (default: './app/static/liveFeed/d.json')
        
        :returns:
            json, file content
    '''
    f = open(path, 'r')
    data = json.load(f)
    return data

@app.route('/getHMJson')
def getHMJson(path='./app/static/liveFeed/heatmap.json'):
    '''
    getJson
        :parameters:
            string, path of th file (default: './app/static/liveFeed/d.json')
        
        :returns:
            json, file content
    '''
    f = open(path, 'r')
    data = json.load(f)
    return data

def getMapNames():
    '''
    getMapNames: Search dir, use folder name as map name, return folder names in list
        :parameters:
            None
        
        :returns:
            list, folder names
    '''
    # TODO: Test@Clariza

    
    path = os.path.join(os.getcwd(),'app','static','maps')
    # dir = '../app/static/maps'
    # # Create directory if not exitst
    if os.path.exists(path):
        print(f"{path}")
    else:
        Path(path).mkdir(parents=True, exist_ok=True)
    maps = []
    try:
        # List all entries in dir
        entries = os.listdir(path)
        for e in entries:
            # only include folders
            if os.path.isdir(os.path.join(path, e)):
                maps.append(e)
    except:
        pass
    return maps
