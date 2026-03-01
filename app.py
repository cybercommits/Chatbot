import os
import time 
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('models/gemini-2.0-flash')
    
    print("🤖 AI is online! Type 'quit' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Chatbot: See you later!")
            break

        try:
            #we use the model to generate a response to YOUR input
            response = model.generate_content(user_input)
            print(f"Gemini: {response.text}")
        except Exception as e:
            if "429" in str(e):
                print("⏳ Rate limit hit! Waiting 30 seconds...")
                time.sleep(30)
            else:
                print(f"❌ AI Error: {e}")