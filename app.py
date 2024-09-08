from flask import Flask, request, send_file, render_template, jsonify
from PIL import Image
import io
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Increase the decompression bomb limit
Image.MAX_IMAGE_PIXELS = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compress', methods=['POST'])
def compress():
    if 'image' not in request.files:
        logging.error('No image uploaded')
        return 'No image uploaded', 400

    file = request.files['image']
    img = Image.open(file.stream)

    # Convert image to RGB mode if necessary
    if img.mode == 'RGBA':
        img = img.convert('RGB')

    # Calculate original size
    file.stream.seek(0, io.SEEK_END)
    original_size = file.stream.tell()
    file.stream.seek(0)  # Reset stream position
    logging.debug(f'Original size: {original_size} bytes')

    img_io = io.BytesIO()
    img.save(img_io, 'JPEG', quality=20)
    compressed_size = img_io.tell()
    logging.debug(f'Compressed size: {compressed_size} bytes')

    if original_size == 0 or compressed_size == 0:
        logging.error('Error in calculating sizes')
        return 'Error in calculating sizes', 500

    compression_percentage = 100 - (compressed_size / original_size * 100)
    logging.debug(f'Compression percentage: {compression_percentage}%')

    img_io.seek(0)
    return jsonify({
        'original_size': original_size,
        'compressed_size': compressed_size,
        'compression_percentage': compression_percentage,
        'download_url': '/download'
    })

@app.route('/download', methods=['POST'])
def download():
    file = request.files['image']
    img = Image.open(file.stream)

    # Convert image to RGB mode if necessary
    if img.mode == 'RGBA':
        img = img.convert('RGB')

    img_io = io.BytesIO()
    img.save(img_io, 'JPEG', quality=20)
    img_io.seek(0)

    return send_file(img_io, mimetype='image/jpeg', as_attachment=True, download_name='compressed_image.jpg')

if __name__ == '__main__':
    app.run(debug=True)