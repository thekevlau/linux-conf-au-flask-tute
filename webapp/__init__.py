"""
WSGI webapp using Flask
"""

from flask import Flask
from flask import redirect, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """Homepage"""
    return "Hello, linux.conf.au"

@app.route('/a-redirect')
def a_redirect():
    return redirect(some_url)

@app.route('/a-template')
def a_template():
    return render_template('template.html')

if __name__ == '__main__':
    app.run(debug=True)
