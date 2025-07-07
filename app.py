import os
from flask import Flask, render_template, request, send_file
from rembg import remove
from PIL import Image
from io import BytesIO

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/remove', methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
        return 'No file part', 400

    file = request.files['image']
    if file.filename == '':
        return 'No selected file', 400

    img_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(img_path)

    # Read & remove background
    input_image = Image.open(img_path).convert("RGBA")
    output = remove(input_image)

    # Force PNG output
    filename_wo_ext = os.path.splitext(file.filename)[0]
    output_filename = f"no_bg_{filename_wo_ext}.png"
    output_path = os.path.join(UPLOAD_FOLDER, output_filename)
    output.save(output_path)

    return render_template('result.html',
                           input_image=file.filename,
                           output_image=output_filename)

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(os.path.join(UPLOAD_FOLDER, filename),
                     as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
