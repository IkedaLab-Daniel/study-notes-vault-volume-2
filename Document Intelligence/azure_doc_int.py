from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

endpoint = os.getenv('AZURE_PROJECT_ENDPOINT')
key = os.getenv('AZURE_API_KEY')
model_id=os.getenv('MODEL_ID')
llm_endpoint  = os.getenv('AZURE_MODEL_PROJECT_ENDPOINT')

def analyze_read():

    with open('./file2.pdf', 'rb') as f:
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
        return result.content

def verify(content):
    client = OpenAI(
        base_url=llm_endpoint,
        api_key=key,
    )

    prompt = f"""
Return True or False only.
Verify if the content below is actually a content of a Securities and Exchange Commission:
{content}
"""

    response = client.responses.create(
        model=model_id,
        input=prompt,
    )

    answer = response.output[0].content[0].text

    # print(f"answer: {answer}")
    return answer

if __name__ == "__main__":
    content = analyze_read()
    answer = verify(content)
    print("Final verification result:", answer)