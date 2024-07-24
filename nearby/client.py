from flask import Flask, request, render_template, send_from_directory
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    files = os.listdir(UPLOAD_FOLDER)
    return render_template('index.html', files=files)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'files[]' not in request.files:
        return 'No file part'
    files = request.files.getlist('files[]')
    for file in files:
        if file.filename == '':
            return 'No selected file'
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    return 'Files uploaded successfully!'

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
