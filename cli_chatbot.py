#!/usr/bin/env python3
"""
Command-line chatbot using Groq API
A simple terminal-based chatbot for quick interactions
"""

import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

class GroqChatbot:
    def __init__(self):
        """Initialize the chatbot with Groq API client"""
        self.groq_client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )
        self.conversation_history = []
        
    def chat(self, user_input):
        """Send user input to Groq and get response"""
        try:
            # Add user message to history
            self.conversation_history.append({
                "role": "user", 
                "content": user_input
            })
            
            # Create messages for the API call
            messages = [
                {
                    "role": "system",
                    "content": "You are a helpful AI assistant. Be conversational, informative, and concise."
                }
            ] + self.conversation_history
            
            # Get response from Groq
            chat_completion = self.groq_client.chat.completions.create(
                messages=messages,
                model="llama3-8b-8192",
                temperature=0.7,
                max_tokens=1024,
                top_p=1,
                stream=False
            )
            
            response = chat_completion.choices[0].message.content
            
            # Add assistant response to history
            self.conversation_history.append({
                "role": "assistant",
                "content": response
            })
            
            return response
            
        except Exception as e:
            return f"Error: {str(e)}"
    
    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []
        print("🧹 Conversation history cleared!")
    
    def show_help(self):
        """Show available commands"""
        print("\n📋 Available commands:")
        print("  /help    - Show this help message")
        print("  /clear   - Clear conversation history")
        print("  /quit    - Exit the chatbot")
        print("  /exit    - Exit the chatbot")
        print("  Just type your message to chat!")
        print()

def main():
    """Main function to run the CLI chatbot"""
    
    # Check if API key is set
    if not os.getenv("GROQ_API_KEY"):
        print("❌ Error: GROQ_API_KEY not found in environment variables.")
        print("Please set your Groq API key in the .env file.")
        return
    
    # Initialize chatbot
    chatbot = GroqChatbot()
    
    # Welcome message
    print("🤖 Welcome to Groq CLI Chatbot!")
    print("Type '/help' for commands or just start chatting!")
    print("Type '/quit' or '/exit' to exit.")
    print("-" * 50)
    
    while True:
        try:
            # Get user input
            user_input = input("\n👤 You: ").strip()
            
            # Handle empty input
            if not user_input:
                continue
            
            # Handle commands
            if user_input.lower() in ['/quit', '/exit']:
                print("👋 Goodbye! Thanks for chatting!")
                break
            elif user_input.lower() == '/help':
                chatbot.show_help()
                continue
            elif user_input.lower() == '/clear':
                chatbot.clear_history()
                continue
            
            # Get chatbot response
            print("🤖 Bot:", end=" ")
            response = chatbot.chat(user_input)
            print(response)
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye! Thanks for chatting!")
            break
        except Exception as e:
            print(f"❌ An error occurred: {str(e)}")

if __name__ == "__main__":
    main()