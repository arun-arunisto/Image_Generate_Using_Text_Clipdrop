import os

from flask import Blueprint, render_template, request, redirect, url_for
import requests

app_bp = Blueprint("app", __name__,
                   template_folder="templates", static_folder='static',
                   static_url_path='/application/static')

#to generate a filename with png extension
def file_name_generate(text):
    if len(text) > 10:
        text = text[:10]
    text_to_generate = str(text).replace(" ", "_")
    filename_with_ext = text_to_generate+".png"
    return filename_with_ext

#to convert the bytes into an output_image
def image_generate_function(image_bytes, output_image):
    try:
        with open(output_image, 'wb') as output_file:
            output_file.write(image_bytes)
        print("Image Created Successfully!!")
    except Exception as e:
        print(e)

@app_bp.route("/")
def home():
    return render_template("index.html")

@app_bp.route("/image_generate", methods=["GET", "POST"])
def image_generate():
    if request.method == "POST":
        text_to_image = request.form["text_to_image"]
        #print(text_to_image)
        image = requests.post('https://clipdrop-api.co/text-to-image/v1',
                              files={
                                  'prompt':(None, text_to_image, 'text/plain')
                              },
                              headers={'x-api-key':os.getenv('API_KEY')})
        if (image.ok):
            output_image = "application/static/images/"+file_name_generate(text_to_image.strip())
            image_bytes = image.content
            image_generate_function(image_bytes, output_image)
        else:
            print(image.raise_for_status())
    return render_template('index.html', data=[{"output_image":file_name_generate(text_to_image.strip())}])

@app_bp.route("/about")
def about():
    return render_template("about.html")

@app_bp.route("/api_reference")
def api_reference():
    return render_template("api_reference.html")