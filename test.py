import os
import main

# image_path = "C:\\Users\spenc\School\picture_book\static\images\\beautiful%20cat%20named%20gseorge\\1.png"

# image_path = image_path.replace(os.sep, "/")





input_string = "beautiful%20cat%20named%20george"
sentences=["cat", "dog", "plane"]
i=0
img_path = os.path.join(os.getcwd(), "\\static\\images\\")
img_path = os.path.join(img_path, input_string.replace(" ", "%20"))
img_path = os.path.join(img_path, f"{i+1}.png")
print(img_path)
if os.path.isfile("../static/images/beautifulcatnamedgeorge/1.png"):
   print("Image file exists!")
else:
    print("Image file not found.")