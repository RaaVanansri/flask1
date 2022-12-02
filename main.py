from flask import Flask, request,render_template
import os
from ip_subnet_calc import subnet

app = Flask(__name__)

def validate(sub,cidr):
    output = ''
    count = 0
    ip = sub.split('.')
    if len(ip) == 4 and 0 < int(cidr) <= 32:
        for i in range(0,4):
            if -1 < int(ip[i]) < 256:
                count += 1
            if count == 4:
                del count
                break
            return True
        else:
            output += ("Entered IP or CIDR is in wrong fromat please enter again")
            return output
    else:
        output += ("Entered IP or CIDR is in wrong fromat please enter again")
        return output


@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        ip = (request.form['textinput']).split('/') 
        if 1 < len(ip) < 3 :
            valid = validate(ip[0],ip[1])
            if valid == True:
                res = subnet(ip[0],ip[1])
                res = res.split('[Begin]')
                param = res[0].split('\n')
                net = res[1].split('\n')
                return render_template('home.html',output = param,netloop = net,v='',sv='hidden')
            else:
                return render_template('home.html',serious = valid,sv='')
        else:
            return render_template('home.html',serious = 'You typed nothing',sv='')
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
