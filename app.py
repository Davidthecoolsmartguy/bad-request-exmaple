from flask import Flask,render_template,flash,request
from wtforms import SubmitField, TextField
from flask.ext.wtf import Form
from wtforms.validators import required


class HourlyRateForm(Form):
    hours_worked = TextField('Hours Worked', [required()] )
    hourly_rate = TextField('Houly Rate', [required()])
    button1 = SubmitField("button1")
    button2 = SubmitField("button2")


app = Flask(__name__)


app.config["SECRET_KEY"] = '1234567890'



@app.route('/',methods=['GET','POST'])

def index():
    form = HourlyRateForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            if request.form['button1'] == "button1":
                flash("button 1 was pressed")
                return render_template('testhere.html', form=form) 

            if request.form['button2'] == "button2":
                flash("button 2 ")
                return render_template('testhere.html', form=form) 
        else:
             flash("NOT VAILD ON SUBMIT")   
             return render_template('testhere.html', form=form) 
    
    elif request.method == 'GET':
        return render_template('testhere.html', form=form) 

if __name__ == '__main__':
    app.run(debug=True)