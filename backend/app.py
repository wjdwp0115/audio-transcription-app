from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 모든 도메인에서의 접근을 허용

@app.route('/')
def index():
    return jsonify({"message": "Hello, World from Audio Transcription Backend!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
