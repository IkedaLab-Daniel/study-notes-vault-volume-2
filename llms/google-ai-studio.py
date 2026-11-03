import os
import time
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

models = [
    {
        "model_name": "Gemma 4 31B",
        "sdk_name": "gemma-4-31b-it",
        "speed-check": "?",
        "i_think": "it's slow - seems like it's always under heavy load cuz it's free",
        "free_quota": "14.4k RPD"
    },
    {

    }
]

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