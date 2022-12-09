from flask import Flask,render_template,request,Response
from macanalysis import macAnalysis
import os

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        file = request.files['File']
        file.save(file.filename)
        if file.filename.split('.')[1] == 'pcapng':
            result = macAnalysis(file.filename)
        else:
            return render_template('home.html',v='')
        os.system(f'rm *.pcapng && rm *.csv')
        return render_template('results.html',outputs = result,v='')

    return render_template('home.html',v='hidden')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port='5000')