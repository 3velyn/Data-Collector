import re
from flask import render_template, request
from data import app, Data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form['email_name']
        height = request.form['height_name']
    return render_template('success.html')

if __name__ == '__main__':
    app.debug == True
    app.run()
