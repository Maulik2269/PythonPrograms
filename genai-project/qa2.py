import sys
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Read document path from command line
if len(sys.argv) < 2:
    print("Usage: python qa.py <pdf_path>")
    sys.exit(1)

pdf_path = sys.argv[1]