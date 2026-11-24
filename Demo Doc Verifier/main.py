from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

endpoint = os.getenv("AZURE_ENDPOINT")
key = os.getenv("AZURE_API_KEY")

def extract_texts_pdf(file_name):
    with open(f'./{file_name}', 'rb') as f:

        document_intelligence_client = DocumentIntelligenceClient(
            endpoint=endpoint,
            credential=AzureKeyCredential(key)
        )

        poller = document_intelligence_client.begin_analyze_document(
            "prebuilt-read", body=f
        )

        result = poller.result()

        # print("Document contents:", result.content)
        return result.content

def verify(content):
    endpoint = ""
    deployment_name = ""

    prompt = f"""
Return only True or False. Check if this content actually relevant to SECURITIES AND EXCHANGE COMMISSION file:
{content}
"""

    client = OpenAI(
        base_url=endpoint,
        api_key=""
    )

    response = client.responses.create(
        model=deployment_name,
        input=prompt,
    )

    # print(f"answer: {response.output[0].content[0].text}")
    return response.output[0].content[0].text


if __name__ == "__main__":
    file_content = extract_texts_pdf('sample-layout.pdf')
    verification_result = verify(file_content)

    print(verification_result)

