from flask import *
import waitress


app = Flask(__name__)

TITLE = "Suvid's Blog"

@app.route('/')
def index():
    return render_template('index.html', title=TITLE)

@app.route('/about')
def about():
    return render_template('about.html', title=TITLE)

@app.route('/contact')
def contact():
    return render_template('contact.html', title=TITLE)



waitress.serve(app, host='0.0.0.0',port=5000)
