from flask import Flask, render_template, request, redirect, url_for, flash
import os
from PIL import Image

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # フラッシュメッセージのために必要

def resize_image(input_path, output_path, size):
    with Image.open(input_path) as img:
        img = img.resize(size, Image.ANTIALIAS)
        img.save(output_path)
        print(f"Image saved to {output_path}")

def resize_images_in_folder(input_folder, output_folder, width, height):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    size = (width, height)
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            resize_image(input_path, output_path, size)

@app.route('/', methods=['GET', 'POST'])
def index():
    errors = {}
    if request.method == 'POST':
        input_folder = request.form['input_folder']
        output_folder = request.form['output_folder']
        width = int(request.form['width'])
        height = int(request.form['height'])

        # フォルダの存在を確認
        if not os.path.exists(input_folder):
            errors['input_folder'] = 'Input folder does not exist.'

        if not os.path.exists(output_folder):
            errors['output_folder'] = 'Output folder does not exist.'

        if not errors:
            resize_images_in_folder(input_folder, output_folder, width, height)
            flash('Images resized successfully!', 'success')
            return redirect(url_for('index'))

    return render_template('index.html', errors=errors)

if __name__ == '__main__':
    app.run(debug=True)