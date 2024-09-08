from flask import Flask, request, send_file, render_template, jsonify
from PIL import Image
import io
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Increase the decompression bomb limit
Image.MAX_IMAGE_PIXELS = None

# Set a maximum file size limit (e.g., 5MB)
MAX_FILE_SIZE = 5 * 1024 * 1024

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compress', methods=['POST'])
def compress():
    if 'image' not in request.files:
        logging.error('No image uploaded')
        return 'No image uploaded', 400

    file = request.files['image']

    # Check file size
    file.stream.seek(0, io.SEEK_END)
    file_size = file.stream.tell()
    file.stream.seek(0)  # Reset stream position

    if file_size > MAX_FILE_SIZE:
        logging.error('File size exceeds limit')
        return 'File size exceeds limit', 400

    img = Image.open(file.stream)

    # Convert image to RGB mode if necessary
    if img.mode == 'RGBA':
        img = img.convert('RGB')

    logging.debug(f'Original size: {file_size} bytes')

    img_io = io.BytesIO()
    img.save(img_io, 'JPEG', quality=20)
    compressed_size = img_io.tell()
    logging.debug(f'Compressed size: {compressed_size} bytes')

    if file_size == 0 or compressed_size == 0:
        logging.error('Error in calculating sizes')
        return 'Error in calculating sizes', 500

    compression_percentage = 100 - (compressed_size / file_size * 100)
    logging.debug(f'Compression percentage: {compression_percentage}%')

    img_io.seek(0)
    return jsonify({
        'original_size': file_size,
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