from flask import render_template, request
from data import app, Data, db
from send_email import send_email
from sqlalchemy.sql import func

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form['email_name']
        height = request.form['height_name']
        user = db.session.query(Data).filter(Data.email_ == email)

        if user.count() == 0:
            data = Data(email, height)
            db.session.add(data)
            db.session.commit()
        else:    
            user.first().height_ = height
            db.session.commit()

        average_height = round(db.session.query(func.avg(Data.height_)).scalar(), 1)
        ppl_count = db.session.query(Data.height_).count()

        send_email(email, height, average_height, ppl_count)
            
        return render_template('success.html')

if __name__ == '__main__':
    app.debug == True
    app.run()
