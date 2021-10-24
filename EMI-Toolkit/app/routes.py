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

from genericpath import exists
from app        import app
from flask      import render_template, request
import json
import os
from pathlib    import Path

@app.route('/tracking/')
def tracking():
    mapName = request.args.get('mapName')
    # measure = request.args.get('measure')
    
    try:
        currPos = getJson()['live']
    except:
        currPos = [0,0]
    return render_template('tracking.html', title='EMI-Toolkit-Tracking', 
                            # measure = measure, 
                            currPos = currPos, mapName=mapName)

@app.route('/heatmap/')
def heatmap():
    mapName = request.args.get('mapName')
    measure = request.args.get('measure')
    try:
        currPos = getJson()['live']
    except:
        currPos = [0,0]

    return render_template('heatmap.html', title='EMI-Toolkit-Heatmap', 
                            measure = measure, 
                            currPos = currPos, mapName=mapName)

@app.route('/index')
def index():
    return render_template('index.html', title='EMI-Toolkit-Home')

@app.route('/')
@app.route('/map')
def map():
    lstMap = getMapNames()
    return render_template('map.html', title='EMI-Toolkit-Map', lstMap=lstMap)

@app.route('/getJson')
def getJson():
    '''
    getJson    
        :returns:
            json, file content
    '''
    try:
        path = os.path.join(os.getcwd(),'app','static','incoming-data','data.json')
        if os.path.exists(path):
            f = open(path, 'r')
            data = json.load(f)
            return data
        else:
            raise FileNotFoundError("data file missing. Check code")
    except Exception as e:
        print(e)


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

    path = os.path.join(os.getcwd(),'app','static','maps')
    # dir = '../app/static/maps'
    # # Create directory if not exitst
    if os.path.exists(path):
        print(f"{path}")
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
    else:
        return []
        

