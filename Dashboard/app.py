from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Requests (needed for Power BI)

# Initialize OpenAI client
client = openai.OpenAI(api_key="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")  # Replace with your OpenAI API key

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")  # Get message from Power BI
    if not user_input:
        return jsonify({"error": "Empty message"}), 400

    try:
        # Send user message to OpenAI GPT model
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        reply = response.choices[0].message.content  # Get chatbot reply
        return jsonify({"reply": reply})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
