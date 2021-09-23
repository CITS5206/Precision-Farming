from app import app
from flask import render_template, redirect, url_for, flash, request
import json
# from datetime import datetime



@app.route('/')
@app.route('/index')
def index():
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

# with open('./out2.json', 'r') as myfile:
#     data = myfile.read()
    

# @app.route('/test')
# def test():
#     jsonfile=json.dumps(data)
#     return jsonfile

@app.route('/test2')
def test2():
    myfile = open('./out2.json', 'r')
    data = myfile.read()
    polylist = []
    datajson = json.loads(data)
    for key in datajson:
        latlonglist = [0,0]
        latlonglist[0] = key
        latlonglist[1] = datajson[key]['LONd']
        polylist.append(latlonglist)
    polylistjson = json.dumps(polylist)
    return polylistjson
