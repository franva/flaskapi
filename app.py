from markupsafe import escape
from flask import Flask


app = Flask(__name__)

@app.route('/<name>')
def maze(name):
    return 'your name is %s' % escape(name)

@app.route('/')
def index():
    return '''
    <html><body><h2>Hello World!<h2></body></html>
    '''

if __name__ == 'main':
    app.run(debug=True)