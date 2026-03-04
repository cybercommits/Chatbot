import os
import time 
import google.generativeai as genai
from dotenv import load_dotenv

#load environment variables
load_dotenv()
api_key = os.getenv("API_KEY")

if api_key:
    genai.configure(api_key=api_key)
    
    #initialize the model with a personality instruction
    model = genai.GenerativeModel(
        model_name='models/gemini-2.0-flash',
        system_instruction="You are a helpful, witty AI assistant."
    )
    
    print("🤖 AI is online! Type 'quit' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Chatbot: See you later!")
            break

        try:
            #generate a response based on user input
            response = model.generate_content(user_input)
            print(f"Gemini: {response.text}")
        except Exception as e:
            if "429" in str(e):
                print("⏳ Rate limit hit! Waiting 30 seconds...")
                time.sleep(30)
            else:
                print(f"❌ AI Error: {e}")
else:
    print("❌ ERROR: API_KEY not found. (Reminder: Recreate your .env file locally!)")