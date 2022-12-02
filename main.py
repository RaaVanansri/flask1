from flask import Flask, request,render_template
import os
from ip_subnet_calc import subnet

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        ip = (request.form['textinput']).split('/')
        res = subnet(ip[0],ip[1])
        splited_res = res.split('\n')
        return render_template('results.html',output = splited_res)
    else:
        return render_template('home.html')

'''@app.route('/results',methods=['GET','POST'])
def results():
    if request.method == 'POST':
        ip = (request.form['textinput']).split('/')
        res = subnet(ip[0],ip[1])
        splited_res = res.replace('\n','<br>')
    return render_template('results.html',output = splited_res)'''


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
