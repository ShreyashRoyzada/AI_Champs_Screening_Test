from flask import Flask,render_template,request
import os
import json
from werkzeug.utils import secure_filename
import pdfplumber
from collections import namedtuple
import shutil

with open('templates\\config.json','r') as c:
    params = json.load(c)["params"]

local_sever = True
app = Flask(__name__)
app.config['UPLOAD_FOLDER']= params['upload_locaion']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/uploader',methods=['GET','POST'])
def uploader():
    if(request.method == 'POST'):
        f= request.files['file1'] 
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        Line = namedtuple('Line','S_no Text')
    comdir = os.path.normpath(os.getcwd() + os.sep + os.pardir)
    os.chdir(comdir+"/Flask API 1/Static")
    i=1 
    lines= []
    for items in os.listdir():
        if(items.endswith('.pdf')):
            file=items
            with pdfplumber.open(file) as pdf:
                text=''
                for page in pdf.pages:
                    text=text+page.extract_text()
                
                lines.append(Line(i,text))
                i=i+1
    
    
    j=json.dumps(lines)
    folder = comdir+"/Flask API 1/Static"
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)   
    return j

app.run(debug=True)