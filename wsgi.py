from flask import Flask, request, send_file

app = Flask(__name__)

"""The app only has one route, which is get-slides. This endpoint receives a PDF file and returns another PDF file with the slides generated."""
@app.route('/get-slides', methods=['POST'])
def get_slides():
    # Get the file from the request
    file = request.files['article']
    # Call the function that generates the slides
    slides = (file)
    # Return the slides
    return send_file(slides, attachment_filename='slides.pdf')