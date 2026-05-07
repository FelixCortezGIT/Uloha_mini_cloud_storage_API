from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return 'home page'

if __name__ == '__main__':
    app.run()
