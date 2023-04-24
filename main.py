from ChatGPT_python import *
from Regular_Expressions_Practice_py import *
from dalle2_python import *
import os
from flask import Flask, render_template, request



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=["GET", "POST"])
def form():
    # input_string = request.form.get("box1").value #Likely source of error
    if request.method == "POST":
         input_string = request.form.get("box1")
    story = start(input_string)
    return f'You entered: {input_string}. {story}'


parentDir = ".\output"


def start(input_string):
    # input_string = input("Enter an outline: ")
    response = generate_response(input_string)

    path = os.path.join(parentDir, input_string)
    os.mkdir(path)
    print(response)
    arrayvalue = parseStory(response) #Setting individual sentences to be a page here
    
    
    begin(arrayvalue, input_string)

        
    # pageNames = np.array(pageNames)

    # for x in pageNames:
    #         print(x)
    # input_string = response
    return f'Story: {input_string}'
    


if (__name__ == '__main__'):
    app.run(debug=True)
