from flask import (
    Flask,
    render_template
)

app = Flask('First app')

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('index.html',title = 'About')

app.run()