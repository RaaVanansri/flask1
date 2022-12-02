from flask import Flask, request,render_template
import os
from ip_subnet_calc import subnet

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        ip = (request.form['textinput']).split('/')
        if 1 < len(ip) < 3 :
            res = subnet(ip[0],ip[1])
            splited_res = res.split('\n')
            return render_template('home.html',output = splited_res,v='',sv='hidden')
        else:
            return render_template('home.html',serious = 'Seriously? Did you just hit enter without type anything in the text field',sv='')
    else:
        return render_template('home.html',v='hidden')

'''@app.route('/results',methods=['GET','POST'])
def results():
    if request.method == 'POST':
        ip = (request.form['textinput']).split('/')
        res = subnet(ip[0],ip[1])
        splited_res = res.replace('\n','<br>')
    return render_template('results.html',output = splited_res)'''


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
