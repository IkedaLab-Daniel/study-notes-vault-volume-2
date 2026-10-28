import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    google_api_key=os.environ["GEMINI_API_KEY"],
)

response = llm.invoke("Hello, Gemini!")

print(response.content)