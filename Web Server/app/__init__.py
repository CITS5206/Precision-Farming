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

from flask              import Flask
from flask_jsglue       import JSGlue

app = Flask(__name__,
        template_folder='~/Applications/emi-toolkit.app/Contents/Resources/templates', 
        static_folder='~/Applications/emi-toolkit.app/Contents/Resources/static')
jsglue = JSGlue(app)



from app import routes
