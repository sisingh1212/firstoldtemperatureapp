from flask import Flask, render_template, request, app
from flask_bootstrap import Bootstrap
from flask_wtf import  Form
from wtforms import StringField, SubmitField, validators
from wtforms.validators import Required, Length

app=Flask(__name__)
app.config['SECRET_KEY']='my secret'
bootstrap=Bootstrap(app)


class myfirstform(Form):
    name=StringField("What is your name", validators=[Required(), Length()])
    submit=SubmitField("Submit")
    
    


@app.route('/', methods=['GET','POST'])
def index():
    name=None
    if request.method == 'POST' and 'name' in request.form:
        name=request.form['name']
        
    return render_template('index.html',name=name)

@app.route('/new/')
def namere():
    months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    
    weather={'Jan':{'min':2,'max':5,'rain':0},
        'Feb':{'min':2,'max':7,'rain':8},
        'Mar':{'min':1,'max':8,'rain':7},
        'Apr':{'min':1,'max':9,'rain':9},
        'Jun':{'min':4,'max':10,'rain':9},
        'May':{'min':4,'max':10,'rain':9},
        'Jul':{'min':1,'max':3,'rain':7},
        'Aug':{'min':2,'max':9,'rain':5},
        'Sep':{'min':5,'max':6,'rain':5},
        'Oct':{'min':6,'max':9,'rain':1},
        'Nov':{'min':3,'max':5,'rain':3},
        'Dec':{'min':1,'max':4,'rain':9}}
    return render_template('error.html', tablename="Months table",months=months, weather=weather, maxx=9, minn=4)
    
    
@app.errorhandler(404)
def nameree(e):
    return render_template('newerror.html')
    
    
        
if __name__=='__main__':
    app.run(debug=True)
