from flask import Flask, render_template, request, jsonify, session
from flask_session import Session
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
app = Flask(__name__)

# Configure Groq API
groq_client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = 'priyanshi'
Session(app)

@app.route('/')
def index():    
    if 'history' not in session:
        session['history'] = []
        welcome_message = "Chatbot: I'm your chatbot powered by Groq! Tell me your queries?"
        session['history'].append({'message': welcome_message, 'sender': 'bot'})
    return render_template('index.html', history=session['history'])

@app.route('/submit', methods=['POST'])
def on_submit():
    query = request.form['query']
    session.setdefault('history', []).append({'message': query, 'sender': 'user'})
    
    try:
        response = generate_response(query)
        response_message = f"Chatbot Response: {response}"
        session['history'].append({'message': response_message, 'sender': 'bot'})
        
        return jsonify({'query': query, 'response': response_message})
    except Exception as e:
        error_message = f"Error: {str(e)}"
        session['history'].append({'message': error_message, 'sender': 'bot'})
        return jsonify({'query': query, 'response': error_message})

def generate_response(query):   
    try:
        # Create a chat completion using Groq
        chat_completion = groq_client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are an intelligent assistant designed to provide accurate and actionable advice. Be helpful, informative, and conversational."
                },
                {
                    "role": "user",
                    "content": query
                }
            ],
            model="llama3-8b-8192",  # Using Llama 3 8B model
            temperature=0.7,
            max_tokens=1024,
            top_p=1,
            stream=False
        )
        
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Sorry, I encountered an error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)