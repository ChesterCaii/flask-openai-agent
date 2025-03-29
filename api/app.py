from flask import Flask, request, jsonify
from flask_cors import CORS
from agent.agent import Agent

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
agent = Agent()

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    prompt = data.get("prompt", "")
    system = data.get("system", "You are a helpful assistant.")
    reply = agent.run(prompt, system)
    return jsonify({"response": reply})

if __name__ == '__main__':
    app.run(debug=True) 