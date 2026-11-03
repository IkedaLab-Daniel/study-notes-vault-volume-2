import os
import time
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY")
)

start_time = time.time()
response = llm.invoke("Hello!! Are you gemini? What model version are you??")
end_time = time.time()

elapsed_time = end_time - start_time

print("--- Response ---")
print(response.content)
print("\n----------------")
print(f"Time elapsed: {elapsed_time:.2f} seconds")