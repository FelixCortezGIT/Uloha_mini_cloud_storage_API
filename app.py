from flask import Flask, request, jsonify, send_from_directory
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
STORAGE_DIR = 'cloud_storage'
os.makedirs(STORAGE_DIR, exist_ok=True)

@app.route('/')
def home():
    return 'home page'

@app.route('/files')
def list_files():
    files = os.listdir(STORAGE_DIR)
    return jsonify(files), 200

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join(STORAGE_DIR, filename))
    return jsonify({"message": "upload succesfull", "filename": filename}), 201

@app.route('/files/<filename>')
def download_file(filename):
    filename = secure_filename(filename)
    return send_from_directory(STORAGE_DIR, filename, as_attachment=True)

@app.route('/files/<filename>', methods=['DELETE'])
def delete_file(filename):
    filename = secure_filename(filename)
    os.remove(os.path.join(STORAGE_DIR, filename))
    return f"file {filename} deleted", 200

if __name__ == '__main__':
    app.run()
