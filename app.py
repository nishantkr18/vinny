from flask import Flask, request, jsonify
from src.bot_state import BotState
from src.bot import Bot
from typing import List, Any

app = Flask(__name__)

# Mock database for storing user information
users = []

@app.route('/newconnect', methods=['GET'])
def newConnect():
    # Create a random username
    username = 'user' + str(len(users) + 1)
    # Store username in users
    users.append(username)
    return jsonify({'username': username}), 200

 
@app.route('/ask', methods=['POST'])
def ask():
    # Get the current user
    current_user = request.get_json().get('username')
    if not current_user:
        return jsonify({'error': 'Username is required'}), 400

    # Get the user input
    input = request.get_json().get('input')
    if not input:
        return jsonify({'error': 'Input is required'}), 400
    
    state = BotState(username=current_user)
    bot = Bot(state=state)
    
    return jsonify({'message': bot.ask(input)}), 200


if __name__ == '__main__':
    app.run()
