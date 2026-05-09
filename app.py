from flask import Flask, request, jsonify
import os

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

if __name__ == '__main__':
    app.run()
