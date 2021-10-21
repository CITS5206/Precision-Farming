'''
 The University of Western Australia : 2021

* CITS5206 Professional Computing

* Group: Precision Farming



* Source Code

* Author: Kiet Hoang

* Date Created: 23-09-2021

* Last Modified: 13-10-2021

* Version: 1.0

* State : Stable 
'''

from app import app
# from math import isclose

if __name__ == "__main__":
    app.run(debug=True)


# @app.context_processor
# def utility_processor():
#     return dict(isclose=isclose)