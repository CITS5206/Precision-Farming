from flask              import Flask
from config             import Config
from flask_sqlalchemy   import SQLAlchemy
from flask_migrate      import Migrate
from flask_jsglue       import JSGlue

app = Flask(__name__)
jsglue = JSGlue(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


from app import routes, models
