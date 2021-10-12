import re
from flask import render_template, request
from data import app, Data, db

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form['email_name']
        height = request.form['height_name']

        if db.session.query(Data).filter(Data.email_ ==  email).count() == 0:
            data = Data(email, height)
            db.session.add(data)
            db.session.commit()
            
            return render_template('success.html')
    return render_template('index.html', text="Seems like we've got something from that email address already!")

if __name__ == '__main__':
    app.debug == True
    app.run()
