import os
import time
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemma-4-31b-it",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

start_time = time.time()
response = llm.invoke("Hello. Are u gemma-4?")
end_time = time.time()

elapsed_time = end_time - start_time

print("--- Response ---")
print(response.content)
print("\n----------------")
print(f"Time elapsed: {elapsed_time:.2f} seconds")