from flask import Flask, jsonify, request
from routes.funciones import funciones_bp

app = Flask(__name__)

app.register_blueprint(funciones_bp)

if __name__ == '__main__':
    app.run(debug=True)