import os
import requests
from google import genai
from dotenv import load_dotenv
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def ai_process(user_input):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=(
                "You are Jarvis, a virtual assistant. "
                "1. Detect the language style of the user's message. "
                "2. If the message is in English, reply in English. "
                "3. If the message is in Hindi, reply in Hindi. "
                "4. If the message is in Gujarati, reply in Gujarati. "
                "5. Keep the tone natural, friendly, and human-like."
                "Always answer in 3 to 4 lines only.\n\n"
                + user_input
            )
        )
        return response.text

    except Exception as e:
        return f"Jarvis Error:{e}"
# test run
if __name__ == "__main__":
    print(ai_process("What is API?"))
