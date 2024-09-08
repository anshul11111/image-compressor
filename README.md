Got it! Here is the content formatted so you can easily copy and paste it directly into a `README.md` file:

```markdown
# Image Compressor

A simple web application to compress images using Flask and Pillow. Users can upload an image, compress it, and download the compressed version. The application also displays the original and compressed image sizes along with the compression percentage.

## Features

- Upload an image to compress
- Display original and compressed image sizes
- Show compression percentage
- Download the compressed image

## Technologies Used

- Python
- Flask
- Pillow (PIL)
- HTML/CSS/JavaScript

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/your-username/image-compressor.git
   cd image-compressor
   ```

2. **Create a virtual environment:**

   ```sh
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```

4. **Install the required packages:**

   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Flask application:**

   ```sh
   python app.py
   ```

2. **Open a web browser and go to:**

   ```
   http://127.0.0.1:5000/
   ```

3. **Upload an image to compress:**

   - Click on the "Choose File" button and select an image.
   - Click on the "Compress" button.

4. **Download the compressed image:**

   - After compression, the original and compressed sizes along with the compression percentage will be displayed.
   - Click on the "Download Compressed Image" button to download the compressed image.

## File Structure

```
image-compressor/
├── app.py
├── requirements.txt
├── render.yaml
├── templates/
│   └── index.html
├── static/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── scripts.js
└── README.md
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
```

You can now copy and paste the above content directly into your `README.md` file.
