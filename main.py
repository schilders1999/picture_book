from ChatGPT_python import *
from Regular_Expressions_Practice_py import *
from dalle2_python import *
import os
import subprocess
import numpy as np
from flask import Flask, render_template, redirect, request, url_for


# chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
# url = "http://localhost:5000/"

# subprocess.Popen([chrome_path, url])


app = Flask(__name__, static_folder = 'static', template_folder='templates', static_url_path='/static')



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['GET','POST'])
def submit():
    if request.method =='POST':
        input_string = request.form['input']
        arrayvalue = start(input_string)
        return pages(input_string, length = len(arrayvalue)) 
    
    

@app.route('/pages', methods=['GET','POST'])
def pages(input_string, length):
    input_string = input_string.replace(" ", "")
    length = length
    return render_template('pages.html', input_string=input_string, length = length)





def start(input_string):
    response = generate_response(input_string)

    path = os.path.join(os.getcwd(), 'static', 'images', input_string.replace(" ", ""))
    os.makedirs(path)
    print(response)
    arrayvalue = parseStory(response) #Setting individual sentences to be a page here
    arrayvalue = np.array(arrayvalue)
    
    begin(arrayvalue, input_string)#DALLE

    txtfile = os.getcwd() + "\\static\\textFiles\\"

    fileName = txtfile + str(input_string.replace(" ", ""))+".txt"
    np.savetxt(fileName, arrayvalue, fmt='%s', newline='\n')
    return arrayvalue
    


if (__name__ == '__main__'):
    app.run(debug=True)

