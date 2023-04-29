from ChatGPT_python import *
from Regular_Expressions_Practice_py import *
from dalle2_python import *
import os
import subprocess
from flask import Flask, render_template, redirect, request, url_for


chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
url = "http://localhost:5000/"

subprocess.Popen([chrome_path, url])


app = Flask(__name__, static_folder = 'static', template_folder='templates', static_url_path='/static')



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    input_string = request.form['input']
    arrayvalue = start(input_string)
    return redirect(url_for('gallery', input_string=input_string, sentences=arrayvalue))



# @app.route('/display', methods=['GET'])
# def display():
#     input_string = request.args.get('input_string')
#     # sentences = request.args.getlist('sentences')
#     # img_path = os.path.join("/static//images", input_string.replace(" ",""))
#     # img_path = os.path.join(img_path, "1.png" )
#     # img_path = img_path.replace("\\","//")

#     image_folder = os.path.join('static/images/' , input_string.replace(" ",""))
#     image_files = [f for f in os.listdir(image_folder) if f.endswith('.png')]
    
#     # Generate a separate page for each image file
#     for i, image_file in enumerate(image_files):
#         image_path = os.path.join(image_folder, image_file)
#         page_filename = f'image_{i}.html'

#         # Render the template with the image path and save as a separate page
#         with app.app_context():
#             rendered_page = render_template('image_template.html', image_path=image_path)
#             with open(page_filename, 'w') as f:
#                 f.write(rendered_page)
    # return render_template('display.html', input_string=input_string, sentences=sentences, img_path=img_path)



@app.route('/gallery')
def gallery():
    input_string = request.args.get('input_string')
    image_dir = os.path.join(app.static_folder, 'images/')
    folder_name = input_string.replace(" ","")
    image_dir = os.path.join(app.static_folder, 'images', folder_name)
    images = sorted(os.listdir(image_dir))
    num_images = len(images)
    pages = [render_template('image_template.html', image=f"{ folder_name }/{images[i]}", prev=i-1, next=i+1) for i in range(num_images)]
    return render_template('gallery.html', pages=pages, image_index=0, num_images=num_images)





def start(input_string):
    response = generate_response(input_string)

    path = os.path.join(os.getcwd(), 'static', 'images', input_string.replace(" ", ""))
    os.makedirs(path)
    print(response)
    arrayvalue = parseStory(response) #Setting individual sentences to be a page here
    
    
    begin(arrayvalue, input_string)
    return arrayvalue
    


if (__name__ == '__main__'):
    app.run(debug=True)



