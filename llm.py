from langchain_google_genai import ChatGoogleGenerativeAI
from config import GOOGLE_API_KEY


try:
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=GOOGLE_API_KEY
    )
    print("LLM initialized")
except Exception as e:
    print("ERROR:", e)