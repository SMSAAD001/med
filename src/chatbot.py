import google.generativeai as genai
from src.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def get_response(user_input):
    """Fetch response from Gemini API."""
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(user_input)
        return response.text if response.text else "⚠️ No response received."
    except Exception as e:
        return f"⚠️ Error: {str(e)}"
