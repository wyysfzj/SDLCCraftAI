# app.py

from flask import Flask, request, jsonify
from LLMServiceManager import LLMServiceManager

app = Flask(__name__)

@app.route('/generate-user-story', methods=['POST'])
def generate_user_story():
    data = request.json
    input_text = data.get('input_text')

    if not input_text:
        return jsonify({'error': 'No input text provided'}), 400

    llm_service_manager = LLMServiceManager()
    user_story = llm_service_manager.handleRequest(input_text)
    return jsonify({'user_story': user_story})

if __name__ == '__main__':
    app.run(debug=True)
