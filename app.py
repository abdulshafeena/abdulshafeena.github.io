
from flask import Flask,redirect,url_for,render_template,request
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
   # print(request.method)
    #print(request.form)
    #return'Hello World'
    if request.method=="POST":
        weight=float(request.form['weight'])
        height=float(request.form['height'])
        cal_bmi=(weight)/(height**2)
        bmi=round(cal_bmi,1)
        if bmi<18.5:
            category='Under weight'
        elif 18.5<=bmi<=24.9:
            category='You are Normal!'
        elif 25<=bmi<=29.9:
            category='Overweight:control your weight'
        else:
            category='Obese:work more'
        data={'bmi':bmi,'category':category}
        return render_template('index.html',data=data)
    return render_template('index.html')
@app.route('/display/<int:name>')
def second(name):
    #print(type(name))
    #return 'you entered:'+str(name)
    if name>50:
        return redirect('http://127.0.0.1:5000/jaya')
    else:
        return redirect('https://dramacool.pa/')
@app.route('/jaya')
def jaya():
    return 'hello!'
@app.route('/marks/<int:num>')
def marks(num):
    if num>=40:
        result='passed!'
        return redirect(url_for('result',result=result))
    else:
        result='failed'
        return redirect(url_for('result',result=result))
@app.route('/result/<result>')
def result(result):
    return 'You are '+result
'''@app.route('/pass')
def presul():
    return 'You are passed!'
@app.route('/fail')
def fail():
    return 'You are failed!'
'''
app.run(use_reloader=True)
