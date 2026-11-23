from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
import numpy as np
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

endpoint = os.getenv('AZURE_PROJECT_ENDPOINT')
key = os.getenv('AZURE_API_KEY')
model_id=os.getenv('MODEL_ID')
llm_endpoint  = os.getenv('AZURE_MODEL_PROJECT_ENDPOINT')

def analyze_read():

    with open('./scannerd.pdf', 'rb') as f:
        document_intelligence_client = DocumentIntelligenceClient(
            endpoint=endpoint,
            credential=AzureKeyCredential(key)
        )

        poller = document_intelligence_client.begin_analyze_document(
            # "prebuilt-read", AnalyzeDocumentRequest(url_source=f)
            "prebuilt-read", body=f
        )

        result = poller.result()

        print("Document contains content: ", result.content)

def verify():
    client = OpenAI(
        base_url=llm_endpoint,
        api_key=key,
    )

    response = client.responses.create(
        model=model_id,
        input="What is the capital of France?",
    )

    print(f"answer: {response.output[0].content[0].text}")

if __name__ == "__main__":
    verify()