from flask import Flask, request, jsonify
from chatbot import TeamChatbot

app = Flask(__name__)
chatbot = TeamChatbot("Bravo Team")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message', '')
    response = chatbot.get_response(message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(port=5000)
