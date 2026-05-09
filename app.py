from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return 'home page'

@app.route('/files')
def list_files():
    files = os.listdir()
    return jsonify(files), 200

if __name__ == '__main__':
    app.run()
