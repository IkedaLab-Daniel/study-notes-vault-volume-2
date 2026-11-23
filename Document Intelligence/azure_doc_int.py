from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
import numpy as np
import os
from dotenv import load_dotenv

load_dotenv()

endpoint = os.getenv('AZURE_PROJECT_ENDPOINT')
key = os.getenv('AZURE_API_KEY')

def analyze_read():
    formUrl = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/sample-layout.pdf"

    document_intelligence_client = DocumentIntelligenceClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key)
    )

    poller = document_intelligence_client.begin_analyze_document(
        "prebuilt-read", AnalyzeDocumentRequest(url_source=formUrl)
    )

    result = poller.result()

    print("Document contains content: ", result.content)

if __name__ == "__main__":
    analyze_read()