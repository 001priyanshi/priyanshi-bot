from flask import Flask, render_template, request, jsonify, session
from flask_session import Session
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()
app = Flask(__name__)
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = 'priyanshi'
Session(app)
@app.route('/')
def index():    
    if 'history' not in session:
        session['history'] = []
        welcome_message = "Chatbot: I'm your chatbot tell me your queries?"
        session['history'].append({'message': welcome_message, 'sender': 'bot'})
    return render_template('index.html', history=session['history'])
@app.route('/submit', methods=['POST'])
def on_submit():
    query = request.form['query']
    session.setdefault('history', []).append({'message': query, 'sender': 'user'})
    
    response = generate_response(query)
    response_message = f"Chatbot Response: {response}"
    session['history'].append({'message': response_message, 'sender': 'bot'})
    
    return jsonify({'query': query, 'response': response_message})
def generate_response(query):   
    qa_prompt = "You are an intelligent  assistant designed to provide accurate and actionable advice."
    input_text = f"{qa_prompt}\nUser question:\n{query}"
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
    result = llm.invoke(input_text)
    return result.content
if __name__ == '__main__':
    app.run(debug=True)