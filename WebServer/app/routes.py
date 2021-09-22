from app    import app
from flask  import render_template

@app.route('/')
@app.route('/tracking')
def index():
    return render_template('tracking.html')