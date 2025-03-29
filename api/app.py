from flask import Flask, request, jsonify
from agent.agent import Agent

app = Flask(__name__)
agent = Agent()

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    prompt = data.get("prompt", "")
    reply = agent.run(prompt)
    return jsonify({"response": reply})

if __name__ == '__main__':
    app.run(debug=True) 