
from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import google.generativeai as genai

# Set up API key
genai.configure(api_key=" ")  # Replace with your actual API key b4 running the code or else the chatbot will show error

MODEL_NAME = "models/gemini-2.0-pro-exp" 
model = genai.GenerativeModel(MODEL_NAME)

app = Flask(__name__)

CORS(app)

@app.route("/chatbot", methods=["POST"])
def chatbot():
    data = request.get_json()
    user_input = data.get("message", "")

    if not user_input:
        return jsonify({"response": "Please enter a valid message."})

    try:
        response = model.generate_content(user_input)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"response": f"Error: {e}"})


if __name__ == "__main__":
    app.run(debug=True)
