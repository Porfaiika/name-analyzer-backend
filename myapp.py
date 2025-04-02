from flask import Flask, request, jsonify
from flask_cors import CORS
import ollama

app = Flask(__name__)
CORS(app)  # เปิดใช้งาน CORS

@app.route('/analyze', methods=['POST'])
def analyze_name():
    data = request.json
    name = data.get("name", "")

    if not name:
        return jsonify({"error": "No name provided"}), 400

    model = "gemma:2b"  # เปลี่ยนมาใช้โมเดล Gemma 2B
    prompt = f"From the name '{name}', how many letters are there? Which letters appear in it?"

    response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
    result = response["message"]["content"]

    return jsonify({"analysis": result})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
