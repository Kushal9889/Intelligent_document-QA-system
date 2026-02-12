# Suppress warnings
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
warnings.filterwarnings('ignore')

# Import standard libraries
import requests

# Import LangChain components (only what we need for now)
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# We'll add these imports later when we need them:
# from langchain.chains import RetrievalQA
# from langchain.prompts import PromptTemplate
# from langchain.chains import ConversationalRetrievalChain
# from langchain.memory import ConversationBufferMemory

# Note: IBM Watsonx imports removed due to Python 3.14 compatibility
# from ibm_watsonx_ai.foundation_models import Model
# from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
# from ibm_watsonx_ai.foundation_models.utils.enums import ModelTypes, DecodingMethods
# from ibm_watson_machine_learning.foundation_models.extensions.langchain import WatsonxLLM

def download_file(url, filename):
    """Download a file from URL"""
    print(f"  → Sending request to: {url}")
    response = requests.get(url)
    print(f"  → Received {len(response.content)} bytes")
    
    with open(filename, 'wb') as f:
        f.write(response.content)
    print(f"  → Saved to: {filename}")

# Main application code goes below
if __name__ == "__main__":
    print("RAG Application Starting...\n")
    
    # Step 1: Download company policies document
    print("Step 1: Downloading document...")
    filename = 'companyPolicies.txt'
    url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/6JDbUb_L3egv_eOkouY71A.txt'
    download_file(url, filename)
    
    # Step 2: Read the file (basic way - for verification)
    print("\nStep 2: Reading file contents...")
    with open(filename, 'r') as file:
        contents = file.read()
        print(f"File size: {len(contents)} characters")
        print(f"First 200 characters:\n{contents[:200]}...")
