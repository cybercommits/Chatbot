import os
import time 
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('models/gemini-2.0-flash')
    
    try:
        response = model.generate_content("Give me a 1-sentence fun fact about space.")
        print(f"🤖 AI Response: {response.text}")
    except Exception as e:
        if "429" in str(e):
            print("⏳ Rate limit reached! Waiting 30 seconds...")
            time.sleep(30)
        else:
            print(f"❌ AI Error: {e}")
else:
    print("❌ ERROR: API_KEY is missing from .env file.")