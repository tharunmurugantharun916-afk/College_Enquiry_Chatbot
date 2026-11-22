from flask import Flask, render_template, request, jsonify
from chatbot import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "")

    if not isinstance(message, str) or not message.strip():
        return jsonify({"response": "Please enter a question."}), 400

    try:
        answer = get_response(message)
        return jsonify({"response": answer})
    except Exception as error:
        app.logger.exception("Chatbot error: %s", error)
        return jsonify({"response": "Sorry, something went wrong. Please try again."}), 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
