from flask import Flask, request, jsonify
from flask_cors import CORS
from agent.agent import Agent

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
agent = Agent()

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    history = data.get("history", [])
    prompt = data.get("prompt", "")
    system = data.get("system", "You are a helpful assistant.")

    # Add system message if it's not already in history
    if not any(msg["role"] == "system" for msg in history):
        history.insert(0, {"role": "system", "content": system})

    # Add the new user message
    history.append({"role": "user", "content": prompt})

    # Get response from agent
    reply = agent.run(history)

    # Add the assistant's response to history
    history.append({"role": "assistant", "content": reply})

    return jsonify({
        "response": reply,
        "history": history
    })

if __name__ == '__main__':
    app.run(debug=True) 